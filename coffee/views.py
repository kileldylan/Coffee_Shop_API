from django.shortcuts import render
from .models import Category, Product, ProductImage, Order, OrderItem, InventoryItem, StockAdjustment, Employee
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer, OrderSerializer, OrderItemSerializer, InventorySerializer, StockAdjustmentSerializer, EmployeeSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
          return [AllowAny()]
        return [IsAdminUser()]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
          return [AllowAny()]
        return [IsAdminUser()]
    
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]
    
class OrderViewSet(viewsets.ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderItemSerializer

   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      return [IsAdminUser()]
   
class OrderItemViewset(viewsets.ModelViewSet):
   queryset = OrderItem.objects.all()
   serializer_class = OrderItemSerializer
   permission_classes = [IsAdminUser]

class InventoryItemViewSet(viewsets.ModelViewSet):
   queryset = InventoryItem.objects.all()
   serializer_class = InventorySerializer
   permission_classes = [IsAdminUser]

class StockAdjustmentViewSet(viewsets.ModelViewSet):
   queryset = StockAdjustment.objects.all()
   serializer_class = StockAdjustmentSerializer
   permission_classes = [IsAdminUser]

class EmployeeViewSet(viewsets.ModelViewSet):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   permission_classes = [IsAdminUser]


