# apps/Patient/urls.py
from django.urls import path
from . import views  # Correct import (use views, not view)

from .views.patient import register_patient, login, view_profile
from apps.Disease.views import view_diseases
from apps.Appointment.views import view_appointments
from apps.Operation.views import view_operations
from apps.Medication.views import view_medications
from apps.Allergy.views import view_allergies
from apps.Patient.view import home_page, patient_list,patient_details

app_name = 'Patient-urls'

urlpatterns = [
    # path('view_diseases',view_diseases, name='view_diseases'),
    path('registration/', register_patient, name='registeration'),
    path('login/', login, name='login'),
    path('profile/<int:pk>/', view_profile, name='view_profile'),
    path('diseases/<str:patient_username>/', view_diseases, name='view_diseases'),
    path('appointments/<str:patient_username>/', view_appointments, name='view_appointments'),
    path('operations/<str:patient_username>/', view_operations, name='view_operations'),
    path('medications/<str:patient_username>/', view_medications, name='view_medications'),
    path('allergies/<str:patient_username>/', view_allergies, name='view_allergies'),

    #Frontend urls
    path('', home_page, name='home'),
    path('patient_list/', patient_list, name='patient_list'), 
    path('patient_details/<int:pk>/', patient_details, name='patient_details'),

]
