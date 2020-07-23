from django.db import models
from django.contrib import auth #offer a lot of authorization tools for accounts
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin): #just to add in def __str__(self) for auth.models.User

    def __str__(self):
        return "@{}".format(self.username) #self.username default attribute of auth.models.User
