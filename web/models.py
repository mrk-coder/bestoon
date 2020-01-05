from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return "{}_Token".format(self.user)


class Expense(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    def __str__(self):
        return "{}--{}".format(self.date, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    def __str__(self):
        return "{}--{}".format(self.date, self.amount)


class passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    time = models.DateTimeField()
    email = models.CharField(max_length=120)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50) #TODO : Do not save password


