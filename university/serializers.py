from rest_framework import serializers

from .models import Student, University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()

    class Meta:
        model = Student
        fields = '__all__'
