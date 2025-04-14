
from rest_framework import serializers
from apps.Patient.models.patient import Patient
from apps.Appointment.models.appointment import Appointment
from apps.Patient.serializer.new import PatientSerializer  # Import PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()  # This will serialize the patient data, including 'username'

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'appointment_time', 'appointment_adress', 'accompany']