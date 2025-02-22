from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Chat(models.Model):
    message = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Session(models.Model):
    summary = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary
