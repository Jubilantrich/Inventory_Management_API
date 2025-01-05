from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import Inventory
from .serializers import InventorySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import logging

logger = logging.getLogger(__name__)

class InventoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"Authorization Header: {request.headers.get('Authorization')}")
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)

        #"Provide sorting options, such as sorting items by Name, Quantity, Price, or Date Added."
        filter_backends = [DjangoFilterBackend, OrderingFilter]
        filterset_fields = ['category', 'price']
        ordering_fields = ['name', 'quantity', 'price', 'date_added']

        return Response(serializer.data)

    def post(self, request):
        logger.info(f"Authorization Header: {request.headers.get('Authorization')}")
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        """
        Handle PUT requests to update an inventory item.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete an inventory item.
        """
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """
        Custom endpoint to filter items with low stock (e.g., quantity < 10).
        """
        low_stock_items = self.get_queryset().filter(quantity__lt=10)
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]