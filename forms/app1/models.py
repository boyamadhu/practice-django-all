from django.db import models

# Create your models here.

class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField()
    date=models.DateField()

    def __str__(self) -> str:
        return self.name
    