from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet, ProductInventoryViewSet, \
                   ProductAddCartItemViewSet, ProductCartViewSet, OrderItemViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('category', ProductCategoryViewSet, basename='category')
router.register('inventory', ProductInventoryViewSet, basename='inventory')
router.register('cart', ProductCartViewSet, basename='cart')
router.register('cart-items', ProductAddCartItemViewSet, basename='cart-items')
router.register('order-items', OrderItemViewSet, basename='order-items')

urlpatterns = [
    path('', include(router.urls)),
]
