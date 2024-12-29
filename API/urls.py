from django.urls import path
from .views import InventoryListCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token Authentication Endpoint
]
