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
        data = request.data
        allMembers = Member.objects.all().values_list('name', flat=True)
        print(allMembers)
        if request.data.get('name') not in allMembers:
            serializer = MemberSerializer(data=data)
            if(serializer.is_valid()):
                # serializer.save()
                Member.objects.create( 
                                    name=serializer.data.get("name"),
                                    phone=serializer.data.get("phone"),
                                    email=serializer.data.get("email"),
                                    address=serializer.data.get("address"),
                                    types=serializer.data.get("types"),
                                    )
                print("Hello W/")
                member = Member.objects.all().values()
                dic = {
                    "msg": "Data Saved Successfully",
                    "data": serializer.data,
                    "status": status.HTTP_201_CREATED
                }
                # return Response(dic)
                return Response(dic)
            print("In Errors")
            dic = {
                "msg": "Data Failed",
                "data": serializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(dic)        
        else:
            dic = {
                "msg": "Duplicate Name",
                "status": 404
            }
            return Response(dic)        
       

# Creating view for TodaysData model
class Today(APIView):
    serializer_class = TodaysDataSerializer
    def get(self,request):
        date = request.GET.get('date')
        shift = request.GET.get('shift')
        print("here data is: ",date)
        print("here shift is: ",shift)
        obj_by_date = TodaysData.objects.filter(date=date,shift=shift )
        # for obj in obj_by_date:
        #     print(obj.fat)
         
        serialized_data =  list(obj_by_date.values())
        return JsonResponse(serialized_data, safe=False)
        
        alldata = TodaysData.objects.all().values()
        return Response({"Message":"Today's Milk Data","Data":alldata})


    def post(self,request):
        print('Request data is :',request.data)
        data = request.data
        name = request.data.get("name")
        print(name)
        # print(name)
        # nam = name_obj.name 
        date = request.data.get("date")
        shift = request.data.get("shift") 
        fat = request.data.get("fat") 
        snf = request.data.get("snf") 
        lit = request.data.get("lit") 
        rate = request.data.get("rate") 
        print(date) 
        print(shift) 
         
        query_set = TodaysData.objects.filter(myname=name,date=date,shift=shift)
        if query_set.exists():
            dic = {
                "msg": "Data with this user name is already filled ",
                "status": 404
            }
            print("query set exist")
            return Response(dic)
        else:
            # serializer = TodaysDataSerializer(data=data)
            # if(serializer.is_valid()):
            #     print("You can fill this Name")
            #     name_obj = Member.objects.get(name=name)
            #     print(name_obj)  
            #     print(name_obj.member_id) 
            #     rate = float(request.data.get('rate')) 
            #     lit = float(request.data.get('lit')) 
            #     amt = int(rate*lit)
            #     print("amount is ",amt)
            #     TodaysData.objects.create( 
            #                         name=name_obj.member_id,
            #                         myname=name_obj.name,
            #                         fat=serializer.data.get("fat"),
            #                         snf=serializer.data.get("snf"),
            #                         rate=serializer.data.get("rate"),
            #                         lit=serializer.data.get("lit"),
            #                         date=serializer.data.get("date"),
            #                         shift=serializer.data.get("shift"),
            #                         tod_amt=amt,
            #                         )
            if name and fat and snf and rate and lit and date and shift:
                print("You can fill this Name")
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
                    dic = {
                        "msg": "Data Saved Successfully",
                        # "data": serializer.data,
                        "status": status.HTTP_201_CREATED
                    }
                    return Response(dic)
                    return Response({"Message":"New data Added","Adding Data ":info})
                

            
            print("serializer not valid")
            dic = {
            "msg": "Data Failed",
            # "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(dic)


             
         
class Payments(APIView):
    serializer_class = PaymentSerializer
    def get(self,request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        # start_date = request.query_params['start_date']
        # end_date = request.query_params['end_date']
        print("here is me :",start_date)
        print(end_date)
        obj_by_dates = Payment.objects.filter(start_date=start_date,end_date=end_date)
        print("hello")
        for obj in obj_by_dates:
            print(obj.myname)
        serialized_data =  list(obj_by_dates.values())
        return JsonResponse(serialized_data, safe=False)
        all = Payment.objects.all().values()
        return Response({"Message":"List of Members", "Member List":all})    

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
            # print(dict)
            serializer_obj = PaymentSerializer(data=dict)
            if(serializer_obj.is_valid()):
                serializer_obj.save()
            else:
                print("error")
        info = Payment.objects.all().values()
        return Response({"Message":"New data Added","Adding Data ":info})
         

        
         






