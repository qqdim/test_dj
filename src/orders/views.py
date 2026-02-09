from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderCreateSerializer
from .services.order_service import create_order

# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        create_order(
            user=self.request.user,
            items=serializer.validated_data["items"]
        )