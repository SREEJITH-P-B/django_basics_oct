from django.db import models
class detailss(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    stream=models.CharField(max_length=30)
    completed=models.BooleanField()
    