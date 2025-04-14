from rest_framework import serializers
from apps.Patient.models.patient import Patient
from apps.Operation.models.operation import Operation
from apps.Patient.serializer.new import PatientSerializer


class OperationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Operation
        fields = ['patient','operation', 'doctor_or_hospital', 'operation_date', 'operation_place', 'operation_costs']