from django.db import models

Type = (
    ('cow','cow'),
    ('buffalo','buffalo'),
)

# Create your models here.
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    phone = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=200,blank=True,null=True)
    types = models.CharField(max_length=100,choices=Type,default=0)
    def __str__(self):
        return self.name
    
     
     
class TodaysData(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE)
    fat = models.DecimalField( max_digits=5, decimal_places=2)
    snf = models.DecimalField( max_digits=5, decimal_places=2)
    rate = models.DecimalField( max_digits=5, decimal_places=2)
    lit = models.DecimalField( max_digits=5, decimal_places=2)
    
    # def __str__(self):
    #     return self.name

Shift = (
    ('morning','morning'),
    ('evening','evening'),
)        
class Payment(models.Model):
    date = models.DateField()
    shift = models.CharField(max_length=50,choices=Shift,default=0)

    
    