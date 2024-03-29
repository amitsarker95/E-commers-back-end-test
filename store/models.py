from django.db import models
from django.utils import timezone


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ProductInventory(models.Model):
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.quantity)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    inventory = models.ForeignKey(ProductInventory , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    

class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    quantiy = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.cart.id} {self.product.name}'

    



