from rest_framework.serializers import ModelSerializer
from .models import User, Blog
from rest_framework import serializers
import re

class UserSeralaizer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if len(data.get("password")) < 8:
            raise serializers.ValidationError({"message": "Parol 8 tadan kam bo'lmasligi kerak"})
        return data
    

class BlogSeralaizer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    
    def validate(self, data):
        # Ismning uzunligi to'g'riligini tekshirish
        name = data.get("name")
        if len(name) < 2 or len(name) > 100:
            raise serializers.ValidationError("Ism kamida 2 ta va ko'pi bilan 100 ta belgidan iborat bo'lishi kerak.")
    
    # Ism faqat harflar, bo'sh joylar, tirnoq va chiziqchalarni o'z ichiga olishi uchun regex
        name_regex = r'^[a-zA-Z\'\- ]+$'
        if not re.match(name_regex, name):
            raise serializers.ValidationError("Ism faqat harflar, bo'sh joylar, tirnoq va chiziqchalarni o'z ichiga olishi mumkin.")
    
        return data
