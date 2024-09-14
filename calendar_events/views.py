from rest_framework import viewsets, filters
from .models import Task
from .serializers import EventSerializer
from .google_calendar import create_google_event, delete_google_event

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description", "date"]

    def perform_create(self, serializer):
        task = serializer.save()
        event_id = create_google_event(task)
        task.google_event_id = event_id
        task.save()

    def perform_destroy(self, instance):
        delete_google_event(instance.google_event_id)
        instance.delete()
