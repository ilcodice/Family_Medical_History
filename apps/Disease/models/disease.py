from django.db import models
from apps.Patient.models.patient import Patient
from apps.Medication.models.medication import Medication
from apps.Medication.models.medication import Medication

class Disease(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    medications = models.ManyToManyField(Medication, related_name='disease')
    disease = models.CharField(max_length=50)
    hereditary = models.CharField(max_length=1,choices=[('y','yes'),('n','no')])
    disease_start_date = models.DateField(blank=True,null=True)


    class Meta:
        db_table = 'diseases'


    def __str__(self):
        patient = Disease.objects.all
        return f'Patient: {self.patient.user} __ Disease: {self.disease}'