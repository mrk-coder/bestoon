from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expense(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)