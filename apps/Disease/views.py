from apps.Disease.serializer import DiseaseSerializer  # Ensure correct path to DiseaseSerializer
from apps.Patient.models import Patient
from apps.Disease.models import Disease
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def view_diseases(request, patient_username):
    # Get the patient instance based on the username
    patient = get_object_or_404(Patient, user__username=patient_username)  # Query by user username
    
    # Get all diseases related to the patient
    diseases = Disease.objects.filter(patient=patient)  # Query diseases for this patient
    
    # Serialize the data
    serializer = DiseaseSerializer(diseases, many=True)
    
    return Response(serializer.data)
