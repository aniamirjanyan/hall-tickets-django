from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Ticket(models.Model):
    seat = models.CharField(max_length=5, primary_key=True)
    t_date = models.DateField(default=timezone.now)
    state = models.BooleanField(default=0)

    def __str__(self):
        return "Ticket " + str(self.seat)


class User(AbstractBaseUser):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    objects = UserManager()

    def __str__(self):
        return str(self.username)

