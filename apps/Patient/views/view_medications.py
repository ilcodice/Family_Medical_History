from rest_framework.decorators import api_view
from apps.Patient.models.patient import Patient
from apps.Medication.models.medication import Medication
from apps.Patient.serializer.patient_medication import MedicationSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

@api_view(['GET'])
def view_medications(request, patient_username):
    try:
        patient = get_object_or_404(Patient,user__username=patient_username)
        medication = Medication.objects.filter(patient=patient)
        serializer = MedicationSerializer(medication, many=True)
        return Response(serializer.data)
    
    except Medication.DoesNotExist:
        return Response({"error":"medication not found for this patient"})