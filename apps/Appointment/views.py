from rest_framework.decorators import api_view
from apps.Appointment.models.appointment import Appointment
from apps.Patient.serializer.new import PatientSerializer
from rest_framework.response import Response
from apps.Appointment.serializer import AppointmentSerializer


@api_view(['GET'])
def view_appointments(request, patient_username):
    try:
        appointment = Appointment.objects.get(patient__user__username=patient_username)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found for this patient."}, status=404)
