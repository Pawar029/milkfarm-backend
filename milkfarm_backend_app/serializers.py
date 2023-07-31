from rest_framework import serializers
from .models import *

# class MemberSerializer(serializers.Serializer):
#     class Meta:
#         model = Member
#         fields = "__all__"

class MemberSerializer(serializers.Serializer):
    # member_id = models.AutoField(primary_key=True,serialize = False)
    name = serializers.CharField(label="Enter Name :")
    phone = serializers.IntegerField(label="Enter Phone No.:")
    email = serializers.CharField(label="Enter Email")
    address = serializers.CharField(label="Address:")
    types = serializers.CharField(label="cow or Buffalo milk:")


# Creating Serializer for Todays Data 
class TodaysDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TodaysData
        fields = "__all__"
    # myname = serializers.CharField(label="Enter Name :")
    # fat = serializers.DecimalField(label="FAT :",max_digits=5, decimal_places=2)
    # snf = serializers.DecimalField(label="SNF :",max_digits=5, decimal_places=2)
    # rate = serializers.DecimalField(label="Rate :",max_digits=5, decimal_places=2)
    # lit = serializers.DecimalField(label="Liter :",max_digits=5, decimal_places=2)
    # date = serializers.DateField(label="Date :")
    # shift = serializers.CharField(label="Shift :")



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
    