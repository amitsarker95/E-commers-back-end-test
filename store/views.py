from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import status
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, ProductCategorySerializer, ProductInventorySerializer, \
                           ProductCartSerializer , ProductCartItemSerializer, AddCartItemSerializer, OrderItemSerializer, \
                           CreateOrderSerializer, OrderSerializer
                           


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductInventoryViewSet(ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCartViewSet(CreateModelMixin,
                         RetrieveModelMixin,
                         GenericViewSet,
                         DestroyModelMixin):
    
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = ProductCartSerializer
    

class ProductAddCartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    queryset = CartItem.objects.all()
    serializer_class = AddCartItemSerializer



class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.data)
        serializer = CreateOrderSerializer(
            data = request.data,
            context = {
                'user_id': self.request.user,
            }
        )
        
        serializer.is_valid(raise_exception = True)
        order = serializer.save()

        return Response(serializer.data)
    



    




