from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile/")


class GarbageType(models.Model):
    name = models.CharField(max_length=255)
    color = models.TextField()

    def __str__(self):
        return self.name


class Garbage(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField(max_length=100)
    description = models.TextField()
    trash_type = models.ForeignKey(GarbageType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Market(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="market/")
    description = models.TextField(max_length=555)
    price = models.IntegerField(max_length=100, default=10)

    def __str__(self):
        return self.title
