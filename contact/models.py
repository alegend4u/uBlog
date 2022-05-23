from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=False, null=False)
    message = models.TextField(null=False, blank=False)