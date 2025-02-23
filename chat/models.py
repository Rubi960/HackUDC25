"""
MIT License

Copyright (c) 2025 HackNCheese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

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
