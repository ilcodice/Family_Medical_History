from django.db import models
from apps.Patient.models.patient import Patient


class Appointment(models.Model):

    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor= models.CharField(max_length=50)
    appointment_date= models.DateField(blank=True, null=True)
    appointment_time= models.TimeField(blank=True, null=True)
    appointment_adress = models.CharField(max_length=60)
    accompany= models.CharField(max_length=30,blank=True, null=True)

    class Meta:
        db_table = 'appointment'


    def __str__(self):
        return f"Name: {self.patient.user}  _  Doctor: {self.doctor}  _  Date: {self.appointment_date}  _  Time: {self.appointment_time}"