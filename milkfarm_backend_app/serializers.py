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
