from rest_framework import serializers
from apps.Medication.models.medication import Medication
from apps.Patient.serializer.patient_diseaes import PatientSerializer


class MedicationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Medication
        fields = ['patient','medication_name', 'medication_type', 'medication_costs','when_to_use']
