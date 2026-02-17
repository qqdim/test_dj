from datetime import datetime, timedelta

from django.db.models import Sum, Count, Avg, Max
from django.db.models.functions import TruncDay
from django.shortcuts import render
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import Order
from users.models import User


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
