from rest_framework import serializers
from .models import Yunalishlar, Teacher, News, Reception

class YunalishlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yunalishlar
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'