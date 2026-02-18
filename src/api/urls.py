from django.urls import path

from api.v1.views import EachDayIncomeAPIView, CustomersStatisticAPIView

urlpatterns=[
    path("statistic/income/", EachDayIncomeAPIView.as_view()),
    path("statistic/customers/", CustomersStatisticAPIView.as_view()),
]