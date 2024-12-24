from apps.Patient.models.patient import Patient
from apps.Disease.models.disease import Disease
from apps.Medication.models.medication import Medication
from apps.Operation.models.operation import Operation
from apps.Allergy.models.allergy import Allergy
from apps.Appointment.models.appointment import Appointment
from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


def patient_details(request, pk):
    patient = Patient.objects.get(id=pk)
    diseases = Disease.objects.filter(patient=patient)
    medications = Medication.objects.filter(patient=patient)
    allergies = Allergy.objects.filter(patient=patient)
    operations = Operation.objects.filter(patient=patient)
    appointments = Appointment.objects.filter(patient=patient)

    return render(request, 'patient_detail.html', {
        'patient': patient,
        'diseases': diseases,
        'medications':medications,
        'allergies':allergies,
        'operations':operations,
        'appointments':appointments
        })



# from django.shortcuts import render, get_object_or_404
# from apps.Patient.models.patient import Patient

# def home_page(request):
#     return render(request, 'home_page.html')

# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request, 'patient_list.html', {'patients': patients})

# def patient_details(request, pk):
#     patient = get_object_or_404(Patient, id=pk)
#     return render(request, 'patient_detail.html', {'patient': patient})
