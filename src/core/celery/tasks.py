from celery import shared_task


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