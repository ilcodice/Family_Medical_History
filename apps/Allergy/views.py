from apps.Allergy.serializer import AllrgySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.Allergy.models.allergy import Allergy
from apps.Patient.models.patient import Patient

@api_view(['GET'])
def view_allergies(request, patient_username):
    try:
        allergy = Allergy.objects.get(patient__user__username=patient_username)
        serializer = AllrgySerializer(allergy)
        return Response(serializer.data)
    except Allergy.DoesNotExist:
        return Response({"error": "Allergy not found for this patient."}, status=404)


