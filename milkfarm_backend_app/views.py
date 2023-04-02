from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
import json
from django.http import JsonResponse
from datetime import date

# Create your views here.
class NewMember(APIView):

    serializer_class = MemberSerializer
    def get(self,request,format=None):
        allMembers = Member.objects.all().values()
        # print(allMembers)
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
        else:
            print("serializer not valid")


# .filter(phone=request.data["phone"])

# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class=AddMemberSerializer

# Creating view for TodaysData model
class Today(APIView):
    serializer_class = TodaysDataSerializer
    def get(self,request):
        date = request.GET.get('date')
        shift = request.GET.get('shift')
        print("here data is: ",date)
        print("here shift is: ",shift)
        obj_by_date = TodaysData.objects.filter(date=date,shift=shift )
        for obj in obj_by_date:
            print(obj.fat)
         
        serialized_data =  list(obj_by_date.values())
        return JsonResponse(serialized_data, safe=False)
        
        alldata = TodaysData.objects.all().values()
        return Response({"Message":"Today's Milk Data","Data":alldata})


    def post(self,request):
        print('Request data is :',request.data)
        name = request.data.get("name") 
        print(name)
        name_obj = Member.objects.get(name=name)
        print(name_obj)  
        print(name_obj.member_id) 
        rate = float(request.data.get('rate')) 
        lit = float(request.data.get('lit')) 
        amt = int(rate*lit)
        print("amount is ",amt)
        # amt = (name_obj.rate) * name_obj.lit 
        dict = {
            "name":name_obj.member_id,
            "myname":name_obj.name,
            "fat":request.data.get("fat"),
            "snf":request.data.get("snf"),
            "rate":request.data.get("rate"),
            "lit":request.data.get("lit"),
            "date":request.data.get("date"),
            "shift":request.data.get("shift"),
            "tod_amt":amt,
        }
        print(dict)
        serializer_obj = TodaysDataSerializer(data=dict)
        if(serializer_obj.is_valid()):
            serializer_obj.save()
            info = TodaysData.objects.all().values()
            return Response({"Message":"New data Added","Adding Data ":info})
        else:
            print("serializer not valid")
         
class Payments(APIView):
    serializer_class = PaymentSerializer
    def get(self,request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        print("here is me :",start_date)
        print(end_date)
        obj_by_date = Payment.objects.filter(start_date = start_date,end_date = end_date )
        for obj in obj_by_date:
            print(obj.amt_of_week)
        serialized_data =  list(obj_by_date.values())
        return JsonResponse(serialized_data, safe=False)
        # all = Payment.objects.all().values()
        # return Response({"Message":"List of Members", "Member List":all})    

    def post(self,request):
        print('Request data is :',request.data)
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        # print("start :",start_date)
        # print("end :",end_date)
        obj_by_date = TodaysData.objects.filter(date__range=(start_date,end_date))
        total = {}
        liter = {}
        all_name = Member.objects.all()
        for n in all_name:
            total[n.name] = 0
            liter[n.name] = 0
        # print(total)
        for ob in obj_by_date:
            temp = str(ob.name)
            amt = int(ob.tod_amt)
            # print(ob.date)
            # print(temp)
            # print(amt)
            lit_of_day = float(ob.lit)
            total[temp] += amt
            liter[temp] += lit_of_day
        # print(total)
        # print(liter)
        for n in all_name:
            temp = str(n.name)
            dict = {
                "name":n.member_id,
                "myname":n.name,
                "start_date":request.data.get("start_date"),
                "end_date":request.data.get("end_date"),
                "amt_of_week":total[temp],
                "lit":liter[temp],
            }
            print(dict)
            serializer_obj = PaymentSerializer(data=dict)
            if(serializer_obj.is_valid()):
                serializer_obj.save()
            else:
                print("error")
        info = Payment.objects.all().values()
        return Response({"Message":"New data Added","Adding Data ":info})
         

        
         






