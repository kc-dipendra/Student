from django.db import models

class Courses(models.Model):
    Course_Name = models.CharField(max_length=255)
    Course_Fees = models.IntegerField()
    Course_Durations = models.IntegerField()
