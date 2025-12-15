from rest_framework import serializers

from .models import StudentModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
