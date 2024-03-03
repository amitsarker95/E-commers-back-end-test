import uuid
from rest_framework import serializers
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id' ,'name', 'description', 'created_at','modified_at']



class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id' ,'quantity', 'created_at', 'modified_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' ,'name', 'description', 'price', 'category', 'inventory']


class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created', 'updated']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        new_uuid = uuid.uuid4()
        instence = Cart.objects.create( id=new_uuid)
        
        return instence




#Cart Items Product Serializers
        

class CartItemsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class ProductCartItemSerializer(serializers.ModelSerializer):
    product = CartItemsProductSerializer()
    total_prices = serializers.SerializerMethodField()

    def get_total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.price
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'total_price']




