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


