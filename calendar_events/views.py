from rest_framework import viewsets, filters, generics
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
        task.google_event_id = event_id
        task.save()


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = EventSerializer

    def perform_destroy(self, instance):
        delete_google_event(instance.google_event_id)
        instance.delete()
