from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product_name","price","quantity")

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("id", "items", "total_price", "status", "created_at")
        read_only_fields = ("id", "total_price", "status", "created_at")

    # def create(self, validated_data):



class OrderItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product_name", "price", "quantity")

class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemReadSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)
    class Meta:
        model = Order
        fields = ("id", "user_email", "status", "total_price", "created_at", "completed_at", "items")
