from django.db import models
from apps.Patient.models.patient import Patient


class Operation(models.Model):
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    operation = models.CharField(max_length=50, blank=True, null=True)
    doctor_or_hospital = models.CharField(max_length=50, blank=True, null=True)
    operation_place = models.CharField(blank=True, null=True)
    operation_date=models.DateField(blank=True, null=True)
    operation_costs = models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        db_table = 'operation'


    def __str__(self):
        return f'Name: {self.patient.user} __ Operation:{self.operation}'