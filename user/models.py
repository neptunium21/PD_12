from django.db import models

class User(models.Model):


    username = models.CharField(max_length=125)
    email = models.CharField(max_length=20)

    # user_id = id(True)                       #var.1

