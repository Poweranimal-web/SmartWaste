from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile/")

