from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import Inventory
from .serializers import InventorySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import logging

# Set up logging for debugging and monitoring
logger = logging.getLogger(__name__)

# API view for managing inventory (list and create)
class InventoryListCreateView(APIView):
    # Ensure only authenticated users can access these endpoints
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve all inventory items with optional filtering and ordering.
        Supports filters like category and price, and ordering by name, quantity, etc.
        """
        logger.info(f"Authorization Header: {request.headers.get('Authorization')}")

        # Extract filter and ordering parameters from query
        category = request.query_params.get('category')
        price = request.query_params.get('price')
        ordering = request.query_params.get('ordering','name')  # Default ordering by name

        # Filter and order the inventory items
        inventory = Inventory.objects.all()
        if category:
            inventory = inventory.filter(category=category)
        if price:
            inventory = inventory.filter(price=price)
        inventory = inventory.order_by(ordering)

        # Serialize and return the filtered/ordered inventory items
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new inventory item with the provided data.
        Ensures that the user provides valid data (e.g., name, quantity, price).
        """
        logger.info(f"Authorization Header: {request.headers.get('Authorization')}")
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view for handling specific inventory items (retrieve, update, delete)
class InventoryDetailView(APIView):
    # Ensure only authenticated users can access these endpoints
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """
        Retrieve a specific inventory item by its ID.
        Returns a 404 error if the item is not found.
        """
        inventory_item = get_object_or_404(Inventory, id=id)
        serializer = InventorySerializer(inventory_item)
        return Response(serializer.data)

    def put(self, request, id):
        """
        Update an existing inventory item by its ID.
        Requires valid data to update the item.
        """
        inventory_item = get_object_or_404(Inventory, id=id)
        serializer = InventorySerializer(inventory_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """
        Delete a specific inventory item by its ID.
        Returns a 204 No Content status if successful.
        """
        inventory_item = get_object_or_404(Inventory, id=id)
        inventory_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ViewSet for managing user accounts
class UserViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD functionality for user accounts.
    Allows anyone to register or view users, but sensitive permissions should be handled separately.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Adjust as needed for sensitive operations
