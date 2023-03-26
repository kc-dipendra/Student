from django.db import models

class Teachers(models.Model):
    Teacher_Name = models.CharField(max_length=255)
    Teacher_Education = models.CharField(max_length=255)
    Teacher_Subject = models.CharField(max_length=255)
