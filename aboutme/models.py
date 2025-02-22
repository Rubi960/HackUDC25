from django.db import models


# Create your models here.
class Analysis(models.Model):
    option = models.CharField(max_length=15)
    result = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
