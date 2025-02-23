from django.db import models


# Create your models here.
class Analysis(models.Model):
    """
    Model for storing user analysis results.
    Input: Model
    Output: Representation of the instance
    """
    option = models.CharField(max_length=15)
    result = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
