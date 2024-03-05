from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import status
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, ProductCategorySerializer, ProductInventorySerializer, \
                           ProductCartSerializer , ProductCartItemSerializer, AddCartItemSerializer, OrderItemSerializer
                           


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
    



    




