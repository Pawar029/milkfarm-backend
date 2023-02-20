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
    # types = serializers.CharField(label="cow or Buffalo milk:")


# Creating Serializer for Todays Data 
class TodaysDataSerializer(serializers.ModelSerializer):
    
    # name = serializers.CharField(label="Enter Name :")
    # fat = serializers.DecimalField(label="Enter Fat:")
    # snf = serializers.DecimalField(label="Enter SNF:")
    # rate = serializers.DecimalField(label="Enter Rate per liter:")
    # lit = serializers.DecimalField(label="Enter Liter of Milk:")

    class Meta:
        model = TodaysData
        fields = "__all__"
    