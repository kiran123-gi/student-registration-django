from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    fee = models.FloatField()
   
    
