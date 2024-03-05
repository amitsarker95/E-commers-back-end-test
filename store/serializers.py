import uuid
from rest_framework import serializers
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem, Order, OrderItem



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id' ,'name', 'description', 'created_at','modified_at']



class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id' ,'quantity', 'created_at', 'modified_at']
        read_only_fields = ['created_at','modified_at' ]
        

class ProductSerializer(serializers.ModelSerializer):
    inventory_size = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    def get_inventory_size(self, product: Product):
            return product.inventory.quantity
    
    def get_category_name(self, product: Product):
        return f'{product.category.name}'
    class Meta:
        model = Product
        fields = ['id' ,'name', 'description', 'price', 'category', 'inventory','inventory_size', 'category_name']

        


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


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    cart_id = serializers.UUIDField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'cart_id', 'quantity']

    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        
        try:
            item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            item.quantity += quantity
            item.save()
            self.validated_data['quantity'] = item.quantity
        except CartItem.DoesNotExist:
            item = CartItem.objects.create(cart_id=cart_id, product_id=product_id, quantity=quantity)
        return item
    

#Order Serializers
    
class SimpleProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class OrderItemSerializer(serializers.ModelSerializer):
     product = SimpleProductSerializers()
     class Meta:
        model = OrderItem
        fields = ['id','product', 'quantity', 'unit_price', ]
        

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','placed_at', 'payment_status_summary']


        
        




