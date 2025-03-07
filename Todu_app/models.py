from django.db import models

# Create your models here.
class  Todu(models.Model):
    titla = models.CharField(max_length=20)
    text =models.TextField(max_length=250)
    date = models.DateField()