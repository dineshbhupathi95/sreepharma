from django.shortcuts import render
from . serializers import *
from rest_framework.generics import ListCreateAPIView
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

class usersinformation(ListCreateAPIView):
    serializer_class = usersinformationserializer
    queryset = Userinfromation.objects.all()