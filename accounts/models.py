#from django.db import models
from django.contrib import auth

# Create your models here.
class Users(auth.models.User):

    def __str__(self):
        return self.username



