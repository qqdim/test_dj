from django.contrib import admin
from .models import Order, OrderItem
from .models import Payment

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at", "completed_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__email",)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product_name", "price", "quantity")
    search_fields = ("product_name",)



# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "amount", "is_success", "paid_at")
    list_filter = ("is_success", "paid_at")