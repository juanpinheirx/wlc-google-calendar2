from rest_framework import serializers
from .models import Task


class EventSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = "__all__"
