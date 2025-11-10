from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    cost_price = models.FloatField()
    in_stock = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    is_primary = models.BooleanField(default=False)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    order_number = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    current_stock = models.IntegerField()
    minimum_stock = models.IntegerField()
    last_restocked = models.DateTimeField()

class StockAdjustment(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    adjustment = models.IntegerField()
    reason = models.TextField()
    adjusted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Employee(models.Model):
    ROLE = [
        ('barista', 'Barista'),
        ('manager', 'Manager'),
        ('cashier', 'Cashier')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE, default='sales')
    hourly_rate = models.IntegerField()
    is_active = models.BooleanField(default=False) 