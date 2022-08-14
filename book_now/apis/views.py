from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDataSerializer
from .models import UserData, UserRegister
from django.shortcuts import render, redirect
from django.http import HttpResponse  
import requests 
import json
import datetime as dt

class UserDataViews(APIView):

    def post(self, request):
        serializer = UserDataSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    if request.method == 'GET':
        return render(request,"home.html")
    else:
        return HttpResponse("yess boss")

def register(request):
    if request.method == 'GET':
        return render(request,"register.html")
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password1')

        obj = UserRegister.objects.create(name = name, email = email, phone = phone, password = password)

        return redirect("http://127.0.0.1:8000/api/login")

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = UserRegister.objects.get(email = email, password = password)
        
        except:
            return HttpResponse("Invalid Credential")
        
        else:
            print(user.pk)
            pk = user.pk
            print(pk)
            return redirect("booking", pk = pk)

def booking(request, pk):

    user = UserRegister.objects.get(pk = pk)
    name = user.name

    if request.method == 'GET':
        return render(request,"booking.html", {'name': name})

    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pickup_date = request.POST.get('pickup_date')
        dropoff_date = request.POST.get('dropoff_date')
        pickup_time = request.POST.get('pickup_time')
        dropoff_time = request.POST.get('dropoff_time')
        pickup_add = request.POST.get('pickup_add')
        dropoff_add = request.POST.get('dropoff_add')

        print(pickup_date)
        date1 = pickup_date.split('-')
        date2 = dropoff_date.split('-')
        if dt.datetime(int(date1[0]),int(date1[1]),int(date1[2])) > dt.datetime(int(date2[0]),int(date2[1]),int(date2[2])):
            return HttpResponse("Dropoff date need to be more than or equal to the dickup date")

        time1 = pickup_time.split(':')
        time2 = dropoff_time.split(':')

        if dt.datetime(int(date1[0]),int(date1[1]),int(date1[2])) == dt.datetime(int(date2[0]),int(date2[1]),int(date2[2])):
            if dt.datetime(2000,1,1,int(time1[0]),int(time1[1])) >= dt.datetime(2000,1,1,int(time2[0]),int(time2[1])):
                return HttpResponse("For the same day, dropoff time need to be more than pickup time")

        try:

            post_url = "http://127.0.0.1:8000/api/user-data/"

            body = {
                "name" : name,
                "email" : email,
                "phone" : phone,
                "pickup_date" : pickup_date,  
                "dropoff_date" : dropoff_date,
                "pickup_time" : pickup_time, 
                "dropoff_time" : dropoff_time,
                "pickup_add" : pickup_add,
                "dropoff_add" : dropoff_add,
            }

            response = requests.post(post_url, data=body)            

            if response.status_code == 200:
                return HttpResponse('{"status" : "success"}')

            else:
                return HttpResponse('{"status" : "Fail"}')

        except:

            return HttpResponse('{"status" : "Fail"}')
            

# class home():
#     def get(request):

#         return render(request,"home.html")

#     def post(request):

#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         pickup_date = request.POST.get('pickup_date')
#         dropoff_date = request.POST.get('dropoff_date')
#         pickup_time = request.POST.get('pickup_time')
#         dropoff_time = request.POST.get('dropoff_time')
#         pickup_add = request.POST.get('pickup_add')
#         dropoff_add = request.POST.get('dropoff_add')

#         try:

#             post_url = "http://127.0.0.1:8000/api/user-data/"

#             body = {
#                 "name" : name,
#                 "email" : email,
#                 "phone" : phone,
#                 "pickup_date" : pickup_date,  
#                 "dropoff_date" : dropoff_date,
#                 "pickup_time" : pickup_time, 
#                 "dropoff_time" : dropoff_time,
#                 "pickup_add" : pickup_add,
#                 "dropoff_add" : dropoff_add,
#             }

#             response = requests.post(post_url, data=body)            

#             # print("\n\n\n\n\n",dir(response),"\n\n\n\n\n")

#             if response.status_code == 200:
#                 return HttpResponse('{"status" : "success"}')

#             else:
#                 return HttpResponse('{"status" : "Fail"}')

#         except:

#             return HttpResponse('{"status" : "Fail"}')
            