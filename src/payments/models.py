from django.db import models
from orders.models import Order


# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    is_success = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for order {self.order.id} - at {self.paid_at}"

