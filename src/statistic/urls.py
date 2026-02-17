from django.urls import path

from orders.urls import urlpatterns
from statistic.views import EachDayIncomeAPIView, CustomersStatisticAPIView

urlpatterns=[
    path("statistic/income/", EachDayIncomeAPIView.as_view(), name="income-30-days"),
    path("statistic/customers/", CustomersStatisticAPIView.as_view(), name="customers-list"),
]