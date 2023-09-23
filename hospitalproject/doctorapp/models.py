from django.db import models

# Create your models here.

class doctortb(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    dr_id=models.AutoField(primary_key=True)
