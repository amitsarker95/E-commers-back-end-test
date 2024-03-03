from django.contrib import admin, messages
from django.db.models.query import QuerySet
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem


admin.site.register(ProductCategory)
admin.site.register(ProductInventory)
# admin.site.register(Product)



class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    low_stock = '<10'
    full_stock = '>10'

    def lookups(self, request, model_admin):
        return [
            (self.low_stock, 'Low'),
            (self.full_stock, 'Full')
        ]
    
    def queryset(self, request, queryset: QuerySet):
        if self.value() == self.low_stock:
            return queryset.filter(inventory__lt=10)
        elif self.value() == self.full_stock:
            return queryset.filter(inventory__gte=10) 
        else:
            return queryset 

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name__istartswith']
    list_display = ['name', 'price', 'category', 'inventory_status', 'product_count']
    list_filter = ['category', 'modified_at', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory.quantity < 10:
            return 'Low'
        else:
            return 'Full'
    @admin.display(ordering='quantity')
    def product_count(self, product):
        total = product.inventory.quantity
        return f'{total}'

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} product(s) were successfully updated.",
            level=admin.messages.SUCCESS
        )
admin.site.register(Product, ProductAdmin)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    search_fields = ['id']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    search_fields = ['id']
    list_display = ['id', 'cart', 'product', 'total_price']
    def total_price(self, cart_item:CartItem):
        return cart_item.quantity * cart_item.product.price
    total_price.short_description = 'Total Price'


