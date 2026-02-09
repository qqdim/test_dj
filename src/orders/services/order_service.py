from django.db import transaction
from orders.models import Order, OrderItem


def create_order(user, items):
    # transaction.atomic
    order = Order.objects.create(user=user)
    total_price = 0

    for item in items:
        price = item["price"]
        quantity = item["quantity"]
        total_price += price * quantity

        OrderItem.objects.create( # bulk_create
            order=order,
            product_name=item["product_name"],
            price=price,
            quantity=quantity,
        )

    order.total_price = total_price
    order.save()

    return order
