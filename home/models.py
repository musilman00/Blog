from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(verbose_name="bio")


    class Meta:
     db_table = "User"

class Blog(models.Model):
   user = models.ForeignKey(to =User,verbose_name="user", on_delete=models.CASCADE)
   name = models.CharField(verbose_name="name", max_length=255)
   info = models.TextField(verbose_name="info")
   date = models.DateField(verbose_name="date", auto_now=True)

   class Meta:
     db_table = "Blog"