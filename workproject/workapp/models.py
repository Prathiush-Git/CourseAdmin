from django.db import models

class register(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    reg_id=models.AutoField(primary_key=True)