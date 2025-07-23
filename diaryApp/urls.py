from django.urls import path
from .views import DiaryListAPIView, DiaryDetailAPIView

urlpatterns = [
    path('', DiaryListAPIView.as_view(), name="diary-list"),
    path('<int:id>/', DiaryDetailAPIView.as_view(), name="diary-detail"),
]
