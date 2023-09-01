from django.db import models
from django.utils import timezone

class todo(models.Model):
    topic = models.CharField(max_length=40)
    venue = models.CharField(max_length=100)
    details = models.TextField()
    slot = models.DateTimeField(default=timezone.now)
    
    

# Create your models here.
