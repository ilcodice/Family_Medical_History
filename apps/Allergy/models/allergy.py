from django.db import models
from apps.Patient.models.patient import Patient
from apps.Medication.models.medication import Medication


YES_NO_CHOICES = [
    ('y', 'Yes'),
    ('n', 'No'),
]

SEASON_CHOICES = [
    ('s', 'Summer'),
    ('w', 'Winter'),
    ('a', 'Autumn'),
    ('sp', 'Spring'),
]


class Allergy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergy_type = models.CharField(max_length=30, blank=True, null= True)#
    medications = models.ManyToManyField(Medication, related_name = 'allergy')
    hereditary = models.CharField(max_length=1, choices=YES_NO_CHOICES)
    seasonal = models.CharField(max_length=1, choices=YES_NO_CHOICES, default='n')
    which_season = models.CharField(max_length=2, choices=SEASON_CHOICES, blank=True, null=True)
    causes = models.CharField(max_length=60, blank=True, null= True)


    class Meta:
        db_table = 'allergy'

    def __str__(self):
        return f"name: {self.patient.user} allergy: {self.allergy_type}"


