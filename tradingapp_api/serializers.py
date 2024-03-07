# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Trading


class TradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading
        fields = ["id", "task", "completed", "timestamp", "updated", "user"]