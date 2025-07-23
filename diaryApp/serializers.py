from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'content', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']