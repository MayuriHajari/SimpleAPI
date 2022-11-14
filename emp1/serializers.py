from .models import Emp
from rest_framework import serializers


class empserializer(serializers.ModelSerializer):
  
  class Meta:
     model=Emp
     fields=['id','name','desc'] 