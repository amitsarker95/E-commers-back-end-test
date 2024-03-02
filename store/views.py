from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem
from .serializers import ProductSerializer, ProductCategorySerializer, ProductInventorySerializer, \
                           ProductCartSerializer , ProductCartItemSerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductInventoryViewSet(ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = ProductCartSerializer

class ProductCartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = ProductCartItemSerializer
    




