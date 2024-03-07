from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


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
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category')
    inventory = models.ForeignKey(ProductInventory , on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    

class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self) -> str:
        return f'{self.cart.id} {self.product.name}'
    


class StoreCustomer(models.Model):
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
    ]
    phone = models.CharField(max_length=15)
    birthdate = models.DateField(null=True)
    member_ship_choices = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES, default = BRONZE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user__username']
        permissions = [
            ('view_history', 'Can view history'),
        ]


class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAIL = 'F'
    PAYMENT_STATUS = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAIL, 'Failed'),
        
    ]
    customer = models.ForeignKey(StoreCustomer, on_delete=models.PROTECT, null=True)
    placed_at = models.DateField(auto_now_add=True)
    payment_status_summary = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PENDING)

    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    
   


    



