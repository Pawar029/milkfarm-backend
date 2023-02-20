from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import viewsets

# Create your views here.
class NewMember(APIView):

    serializer_class = MemberSerializer
    def get(self,request):
        allMembers = Member.objects.all().values()
        return Response({"Message":"List of Members", "Member List":allMembers})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj = MemberSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Member.objects.create( 
                                name=serializer_obj.data.get("name"),
                                phone=serializer_obj.data.get("phone"),
                                email=serializer_obj.data.get("email"),
                                address=serializer_obj.data.get("address"),
                                # types=serializer_obj.data.get("types"),
                                )
# .filter(phone=request.data["phone"])
        member = Member.objects.all().values()
        return Response({"Message":"New member Added", "AddMember":member})


# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class=AddMemberSerializer

# Creating view for TodaysData model
class Today(APIView):
    serializer_class = TodaysDataSerializer
    def get(self,request):
        alldata = TodaysData.objects.all().values()
        return Response({"Message":"Today's Milk Data","Data":alldata})


    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj = TodaysDataSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            TodaysData.objects.create( 
                                name=serializer_obj.data.get("name"),
                                fat=serializer_obj.data.get("fat"),
                                snf=serializer_obj.data.get("snf"),
                                rate=serializer_obj.data.get("rate"),
                                lit=serializer_obj.data.get("lit"),
                                # types=serializer_obj.data.get("types"),
                                )
 
        info = TodaysData.objects.all().values()
        return Response({"Message":"New data Added","Adding Data ":info})




