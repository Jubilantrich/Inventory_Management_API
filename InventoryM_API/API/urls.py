from django.urls import path
from .views import InventoryListCreateView

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
]
