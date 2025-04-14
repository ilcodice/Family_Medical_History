from rest_framework import serializers
from apps.Patient.models.patient import Patient
from django.core.validators import RegexValidator



class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    phone_number = serializers.CharField()
    date_of_birth = serializers.DateField()
    current_city = serializers.CharField()
    gender = serializers.CharField()

    def create(self, validated_data):
        return Patient.objects.get_or_create(**validated_data) # if it exists get it if not create it