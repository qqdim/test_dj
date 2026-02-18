
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE, related_name="orders")

    class Status(models.TextChoices):
        CREATED = "created", "Created"
        IN_PROGRESS = "in_progress", "In progress"
        COMPLETED = "completed", "Completed"
        OVERDUE = "overdue", "Overdue"

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.CREATED,
        db_index=True
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["status", "created_at"]),
        ]

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")

    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"



class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    is_success = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for order {self.order.id} - at {self.paid_at}"

