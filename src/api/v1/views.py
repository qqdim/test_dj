from datetime import timedelta

from django.db.models import Sum, Count, Avg, Max
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Order
from core.models import User


# Create your views here.
class EachDayIncomeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        today = timezone.now()
        start_date = today - timedelta(days=30)
        queryset = (
            Order.objects.filter(status=Order.Status.COMPLETED, created_at__gte=start_date)
            .values("created_at__date")
            .annotate(income=Sum("total_price"))
            .order_by("day")
        )
        return Response(queryset)


class CustomersStatisticAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = (
            User.objects
            .annotate(orders_count=Count("orders"),
                      avg_order_price=Avg("orders__total_price"),
                      last_order_date=Max("orders__created_at"))
            .values("email", "orders_count", "avg_order_price", "last_order_date")
        )
        return Response(queryset)

from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Order
from core.serializers import OrderCreateSerializer, OrderListSerializer
from core.order_service import create_order

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