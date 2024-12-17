from rest_framework import serializers
from apps.Disease.models import Disease
from apps.Patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')  # Access 'username' through 'user'

    class Meta:
        model = Patient
        fields = ['username']
# Disease serializer that includes the patient info.
class DiseaseSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()  # This line tells the serializer to include the serialized Patient data inside the Disease serializer.

    class Meta:
        model = Disease #This specifies that we are serializing data from the Disease model.
        fields = ['patient', 'disease'] 


