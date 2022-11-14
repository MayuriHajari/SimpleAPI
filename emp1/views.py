from urllib import response
from urllib.request import Request
from django.http import JsonResponse
from .models import Emp
from .serializers import empserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from emp1 import serializers

@api_view(['GET','POST'])
def emp_list(request):
     #get all emp
     #serialize them
     # return json
     if request.method=='GET':
        emp = Emp.objects.all()
        serializer= empserializer(emp, many=True)
        return Response({'emp':serializer.data})
     
     if request.method=='POST':
          serializer= empserializer(data= request.data)
          if serializer.is_valid():
               serializer.save()
               messages.success(request,"Record added successfully!!")
               return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view (['GET','PUT','DELETE'])  
def emp_detail(request, id):

     try:
          emp= Emp.objects.get(pk=id)
     except Emp.DoesNotExist:
           return Response(status=status.HTTP_404_NOT_FOUND)

     if request.method=="GET":
        serializers= empserializer(emp)
        return Response(serializers.data)

     elif request.method=="PUT":
          serializers = empserializer(emp,data=request.data)

          if serializers.is_valid()==True: 
             serializers.save()
             return Response(serializers.data)
          return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)      

     elif request.method=='DELETE':    
          emp.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)   

     