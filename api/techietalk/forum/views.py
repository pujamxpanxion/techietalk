# appname/views.py
from django.shortcuts import render
 
from rest_framework import viewsets
from .models import Category, Forum
from .serializers import CategorySerializer, ForumSerializer
 
class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer