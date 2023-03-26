from django.db import models

class Admins (models.Model):
    Login_name = models.CharField(max_length=255)
    Login_password = models.CharField(max_length=255)
