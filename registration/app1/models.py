from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    adress=models.TextField()
    Profile_pic=models.ImageField(upload_to='sab')

    def __str__(self) -> str:
        return self.adress