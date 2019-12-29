from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    def __str__(self):
        return "{}--{}".format(self.date, self.amount)


class Incomme(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    def __str__(self):
        return "{}--{}".format(self.date, self.amount)