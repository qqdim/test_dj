from django.urls import path
from api.v1.views import CustomersStatisticAPIView, EachDayIncomeAPIView, OrderCreateAPIView, OrderListAPIView

urlpatterns = [
    path("orders/", OrderCreateAPIView.as_view() ),
    path("orders/list/", OrderListAPIView.as_view() ),

    path("statistic/income/", EachDayIncomeAPIView.as_view()),
    path("statistic/customers/", CustomersStatisticAPIView.as_view()),
]
