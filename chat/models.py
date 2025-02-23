from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Chat(models.Model):
    """
    Chat model for storing user messages and responses.

    Input: Model
    Output: Representation of the instance
    """
    message = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Session(models.Model):
    """
    Session model for storing user messages and responses.

    Input: Model
    Output: Representation of the instance
    """
    summary = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary

class History(models.Model):
    """
    History model for managing user historic messages.

    Input: Model
    Output: Representation of the instance
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    history = models.JSONField(default=list)

    def append(self, message):
        tmp = self.history
        tmp.append(message)
        self.history = tmp
        self.save()

    def __str__(self):
        return self.history
