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
    address = models.CharField(max_length=200,null=True)
    types = models.CharField(max_length=100,choices=Type,default=0)
    
    def __str__(self):
        return self.name
    

Shift = (
    ('morning','morning'),
    ('evening','evening'),
)     
     
class TodaysData(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE)
    myname = models.CharField( max_length=50, default=0)
    fat = models.DecimalField( max_digits=5, decimal_places=2)
    snf = models.DecimalField( max_digits=5, decimal_places=2)
    rate = models.DecimalField( max_digits=5, decimal_places=2)
    lit = models.DecimalField( max_digits=5, decimal_places=2)
    date = models.DateField(auto_now=False, auto_now_add=False)
    shift = models.CharField(max_length=50,choices=Shift,default=0)
    tod_amt = models.IntegerField(default=0)
    # def __str__(self):
    #     return self.name

        
class Payment(models.Model):
    amt_of_week = models.IntegerField(default=0)
    myname = models.CharField( max_length=50, default=0)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    lit = models.DecimalField( max_digits=5, decimal_places=2,default=0)
    # dates = models.DateField(null=True,blank=True)
    name = models.ForeignKey(Member, on_delete=models.CASCADE)



    
    