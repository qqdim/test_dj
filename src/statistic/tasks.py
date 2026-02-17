from config.celery import app
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum
from orders.models import Order

@shared_task
def daily_revenue_report():
    print("work")
    # today = timezone.now().date()
    # start = today - timedelta(days=1)
    #
    # revenue = (
    #     Order.objects
    #     .filter(
    #         status=Order.Status.COMPLETED,
    #         created_at__date=start
    #     )
    #     .aggregate(total=Sum("total_price"))
    # )
    #
    # print(f"Revenue for {start}: {revenue['total']}")