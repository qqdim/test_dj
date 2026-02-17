from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer
from .services.order_service import create_order

# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        create_order(
            user=self.request.user,
            items=serializer.validated_data["items"]
        )

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.select_related("user").prefetch_related("items")
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("status", "created_at")
    ordering_fields = ("created_at",)
    ordering = ("-created_at",)