from django.urls import path, include
from .views import InventoryListCreateView, UserViewSet, InventoryDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


# Define the router for ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

# Define urlpatterns for class-based views and include router URLs
urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(), name='inventory-list-create'),  # For class-based views
    path('inventory/<int:id>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # For obtaining auth tokens
    path('', include(router.urls)),  # Include ViewSet route
]

# Include user endpoints from the router
urlpatterns += router.urls
