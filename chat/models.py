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

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    history = models.TextField()

    def get_history_list(self):
        return self.history.split("|||") if self.history else []

    def set_history_list(self, messages):
        self.history = "|||".join(messages)

    def append(self, message):
        tmp = self.get_history_list()
        tmp.append(message)
        self.set_history_list(tmp)

    def __str__(self):
        return self.history
