from rest_framework import serializers
from .models import Category, Product, ProductImage, Order, OrderItem, InventoryItem, StockAdjustment, Employee

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['cost_price']

class ManagerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class StockAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'