from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.TextField()
    activate = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)