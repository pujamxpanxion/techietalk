# appname/serializers.py, this file was created manually
from rest_framework import serializers
from .models import Category, Forum
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
 
class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'