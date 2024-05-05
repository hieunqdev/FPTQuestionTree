from django.db import models
# import schedule
# import time

# Create your models here.
class Question(models.Model):
    name = models.TextField()
    activate = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class QuestionQueue(models.Model):
    command = models.CharField()
    url = models.CharField()
    data = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # def job():
    #     print("I'm working...")

    # schedule.every(0.1).minutes.do(job) 
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

class Partner(models.Model):
    name = models.CharField()
    activate = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)