from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    phone = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=200,blank=True,null=True)
    # types = models.CharField(max_length=100,choices=
    #                         (('cow','cow'),
    #                          ('buffalo','buffalo')))


class TodaysData(models.Model):
    name = models.CharField(max_length=50)
    fat = models.DecimalField( max_digits=5, decimal_places=2)
    snf = models.DecimalField( max_digits=5, decimal_places=2)
    rate = models.DecimalField( max_digits=5, decimal_places=2)
    lit = models.DecimalField( max_digits=5, decimal_places=2)
    