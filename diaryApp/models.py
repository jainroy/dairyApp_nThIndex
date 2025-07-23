from django.db import models
from authentication.models import User

class Diary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diary_entries')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.owner.username}'s diary on {self.created_at} & updated at {self.updated_at}: {self.title}"
