# apps/Patient/urls.py

from django.urls import path
from . import views  # Correct import (use views, not view)
from .views.patient import register_patient, login, view_profile
from apps.Patient.views.view_disease import view_diseases
from apps.Patient.views.view_appointments import view_appointments
from apps.Patient.views.view_operations import view_operations
from apps.Patient.views.view_medications import view_medications
from apps.Patient.views.view_allergies import view_allergies
from apps.Patient.view import home_page, patient_list,patient_details

app_name = 'patient-urls'

urlpatterns = [
    path('registration/', register_patient, name='registeration'),
    path('login/', login, name='login'),
    path('view_profile/<int:pk>/', view_profile, name='view_profile'),
    path('view_diseases/<str:patient_username>/', view_diseases, name='view_diseases'),
    path('view_appointments/<str:patient_username>/', view_appointments, name='view_appointments'),
    path('view_operations/<str:patient_username>/', view_operations, name='view_operations'),
    path('view_medications/<str:patient_username>/', view_medications, name='view_medications'),
    path('view_allergies/<str:patient_username>/', view_allergies, name='view_allergies'),

    #Frontend urls
    path('', home_page, name='home'),
    path('patient_list/', patient_list, name='patient_list'), 
    path('patient_details/<int:pk>/', patient_details, name='patient_details'),

]
