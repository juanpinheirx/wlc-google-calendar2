from rest_framework import generics
from .models import Task
from .serializers import EventSerializer
from .google_calendar import create_google_event, delete_google_event
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        try:
            event_id = create_google_event(task)
            task.google_calendar_id = event_id
            task.save()
        except Exception as e:
            task.delete()
            raise e


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = EventSerializer

    def perform_destroy(self, instance):
        try:
            delete_google_event(instance.google_calendar_id)
        except Exception as e:
            raise e
        instance.delete()


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Este é um dado protegido!")
