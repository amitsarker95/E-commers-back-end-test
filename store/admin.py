from django.contrib import admin, messages
from django.db.models.query import QuerySet
from .models import Product, ProductCategory, ProductInventory, Cart, CartItem


# admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductInventory)
admin.site.register(Cart)
admin.site.register(CartItem)


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
        return queryset.filter(inventory__gt=10)
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name__istartswith']
    actions = ['clear_inventory']
    list_display = ['name', 'price', 'inventory_status', 'category']
    list_filter = ['category', 'modified_at', InventoryFilter]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Full'
    

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} product's were successfully updated.",
            messages.SUCCESS
        )