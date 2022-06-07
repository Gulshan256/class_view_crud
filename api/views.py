from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import student
from .serializer import studentSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.

class studentList(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer 

class studentDetail(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer


