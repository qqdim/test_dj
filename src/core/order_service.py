from django.db import transaction
from core.models import Order, OrderItem


def create_order(user, items):
    with transaction.atomic():
        order = Order.objects.create(user=user)
        order_items = []
        total_price = 0

        for item in items:
            price = item["price"]
            quantity = item["quantity"]
            total_price += price * quantity

            order_items.append(OrderItem(
                order=order,
                product_name=item["product_name"],
                price=price,
                quantity=quantity )
            )
        OrderItem.objects.bulk_create(order_items)
        order.total_price = total_price
        order.save()

    return order
