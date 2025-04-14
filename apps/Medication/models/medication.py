from django.db import models
from multiselectfield import MultiSelectField
from apps.Patient.models.patient import Patient
    

class Medication(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name=models.CharField(max_length=50)
    medication_type=models.CharField(max_length=50)
    medication_costs=models.CharField(max_length=20,default="0")
    when_to_use=MultiSelectField(choices=[('m','morning'),('m','midday'),('n','night')])

    class Meta:
        db_table = 'medications'

    def __str__(self):
        return f'Patient: {self.patient.user} __ Medication: {self.medication_name}'

    

