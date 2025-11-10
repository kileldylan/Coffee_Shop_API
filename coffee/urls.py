from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import CategoryViewSet, ProductViewSet, ProductImageViewSet, OrderViewSet, OrderItemViewset, InventoryItemViewSet, StockAdjustmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'product_image', ProductImageViewSet, basename='product_image')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order_item', OrderItemViewset, basename='order_item')
router.register(r'inventory', InventoryItemViewSet, basename='inventory')
router.register(r'stock_adjustment', StockAdjustmentViewSet, basename='stock_adjustment')
router.register(r'employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]