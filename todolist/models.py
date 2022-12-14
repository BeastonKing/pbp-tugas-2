from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.db.models.deletion import CASCADE
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    title = models.TextField()
    description = models.TextField()