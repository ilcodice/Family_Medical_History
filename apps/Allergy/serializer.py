from rest_framework import serializers
from apps.Patient.serializer.new import PatientSerializer
from apps.Allergy.models.allergy import Allergy

class AllrgySerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Allergy
        fields = ('patient','allergy_type','medications','hereditary','seasonal','which_season','causes')
