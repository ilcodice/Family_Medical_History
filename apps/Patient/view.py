from django.shortcuts import render
from apps.Patient.models.patient import Patient
from apps.Disease.models.disease import Disease
from apps.Medication.models.medication import Medication
from apps.Allergy.models.allergy import Allergy
from apps.Operation.models.operation import Operation
from apps.Appointment.models.appointment import Appointment

# In apps/Patient/view.py
from django.template.loader import render_to_string
from django.http import HttpResponse


def home_page(request):
    """Render home page"""
    return render(request, 'home_page.html')

def patient_list(request):
    """List all patients with debug information"""
    patients = Patient.objects.select_related('user').all()
    
    # Debug output (check server console)
    print(f"Found {patients.count()} patients")
    if patients.exists():
        first_patient = patients.first()
        print(f"First patient: {first_patient.user.first_name} {first_patient.user.last_name}")
    
    return render(request, 'patient_list.html', {'patients': patients})

def patient_details(request, pk):
    """Show detailed view for a single patient"""
    patient = Patient.objects.select_related('user').get(id=pk)
    diseases = Disease.objects.filter(patient=patient)
    medications = Medication.objects.filter(patient=patient)
    allergies = Allergy.objects.filter(patient=patient)
    operations = Operation.objects.filter(patient=patient)
    appointments = Appointment.objects.filter(patient=patient)

    return render(request, 'patient_detail.html', {
        'patient': patient,
        'diseases': diseases,
        'medications': medications,
        'allergies': allergies,
        'operations': operations,
        'appointments': appointments
    })

# from apps.Patient.models.patient import Patient
# from apps.Disease.models.disease import Disease
# from apps.Medication.models.medication import Medication
# from apps.Operation.models.operation import Operation
# from apps.Allergy.models.allergy import Allergy
# from apps.Appointment.models.appointment import Appointment
# from django.shortcuts import render

# def home_page(request):
#     return render(request, 'home_page.html')

# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request, 'patient_list.html', {'patients': patients})


# def patient_details(request, pk):
#     patient = Patient.objects.get(id=pk)
#     diseases = Disease.objects.filter(patient=patient)
#     medications = Medication.objects.filter(patient=patient)
#     allergies = Allergy.objects.filter(patient=patient)
#     operations = Operation.objects.filter(patient=patient)
#     appointments = Appointment.objects.filter(patient=patient)

#     return render(request, 'patient_detail.html', {
#         'patient': patient,
#         'diseases': diseases,
#         'medications':medications,
#         'allergies':allergies,
#         'operations':operations,
#         'appointments':appointments
#         })



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
