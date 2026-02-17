from django.urls import path
from .views import OrderCreateAPIView, OrderListAPIView

urlpatterns = [
    path("orders/", OrderCreateAPIView.as_view() ),
    path("orders/list/", OrderListAPIView.as_view() ),
]
