from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Diary
from .serializers import DiarySerializer

class DiaryListAPIView(ListCreateAPIView):
    serializer_class = DiarySerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Diary.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class DiaryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiarySerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Diary.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)