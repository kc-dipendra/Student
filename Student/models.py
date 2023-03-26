from django.db import models

class Students(models.Model):
    Name = models.CharField(max_length=255)
    Roll = models.IntegerField()
    Age = models.IntegerField()
    Address = models.CharField(max_length=255)
    Phone = models.IntegerField()
