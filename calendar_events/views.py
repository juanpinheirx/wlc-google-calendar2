from rest_framework import generics
from .models import Task
from .serializers import EventSerializer
from .google_calendar import create_google_event, delete_google_event

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        event_id = create_google_event(task)
        task.google_calendar_id = event_id
        task.save()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = EventSerializer

    def perform_destroy(self, instance):
        delete_google_event(instance.google_calendar_id)
        instance.delete()
