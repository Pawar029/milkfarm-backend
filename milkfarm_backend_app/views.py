from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class NewMember(APIView):

    serializer_class = MemberSerializer
    def get(self,request,format=None):
        allMembers = Member.objects.all().values()
        return Response({"Message":"List of Members", "Member List":allMembers})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj = MemberSerializer(data=request.data)
        if(serializer_obj.is_valid()):
        #     serializer_obj.save()
        #     return Response({'msg':'Data Created'},serializer_obj.data,status=status.HTTP_201_CREATED)
        # return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)            

            Member.objects.create( 
                                name=serializer_obj.data.get("name"),
                                phone=serializer_obj.data.get("phone"),
                                email=serializer_obj.data.get("email"),
                                address=serializer_obj.data.get("address"),
                                types=serializer_obj.data.get("types"),
                                )
        member = Member.objects.all().values()
        return Response({"Message":"New member Added", "AddMember":member})

# .filter(phone=request.data["phone"])

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
        print('Request data is :',request.data)
        # name_ID = request.data.get("name")
        # print(name_ID)
        # member_obj = Member.objects.get(name = name_ID)

        # print(member_obj.member_id)
        # print(member_obj.phone)
        # print(member_obj)
        name_id = request.data.get("name")
        print(name_id)
        name = Member.objects.get(id=name_id)  
        print(name)  
        serializer_obj = TodaysDataSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            # name_id = request.data.get("name")
            # print(name_id)
            # name = Member.objects.get(id=name_id)
            # print(name)
            TodaysData.objects.create( 
                                name=name,
                                # **serializer_obj.validated_date
                                fat=serializer_obj.data.get("fat"),
                                snf=serializer_obj.data.get("snf"),
                                rate=serializer_obj.data.get("rate"),
                                lit=serializer_obj.data.get("lit"),
                                # types=serializer_obj.data.get("types"),
                                )
            # return Response(TodaysDataSerializer(temp).data)
        info = TodaysData.objects.all().values()
        return Response({"Message":"New data Added","Adding Data ":info})
        # else:
        #     return Response(serializer_obj.errors,status=400)
        # info = TodaysData.objects.all().values()
        # return Response({"Message":"New data Added","Adding Data ":info})


class Payments(APIView):
    serializer_class = PaymentSerializer
    def post(self,request):
        print('Requested data is :', request.data)
        serializer_obj = PaymentSerializer(data = request.data)
        if(serializer_obj.is_valid()):
            Payment.objects.create(
                    date =  serializer_obj.data.get('date'),
                    shift =  serializer_obj.data.get('shift'),
            )

        info = Payment.objects.all().values()
        return Response({"Message": "New Data Added","Data is Adding":info})






