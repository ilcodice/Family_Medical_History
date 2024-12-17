from django.urls import path
from .views.patient import register_patient, login, view_profile
from apps.Patient.views.view_disease import view_diseases
from apps.Patient.views.view_appointments import view_appointments
from apps.Patient.views.view_operations import view_operations
from apps.Patient.views.view_medications import view_medications
from apps.Patient.views.view_allergies import view_allergies


app_name = 'Patient'
urlpatterns = [
        path('registration/', register_patient, name='registeration'),#/api/v1/patient/registration/
        path('login/', login, name='login'),
        path('view_profile/<int:pk>/', view_profile, name='view_profile'),
        path('view_diseases/<str:patient_username>/', view_diseases, name='view_diseases'),
        path('view_appointments/<str:patient_username>/',view_appointments, name='view_appointments'),
        path('view_operations/<str:patient_username>/',view_operations, name='view_operations'),
        path('view_medications/<str:patient_username>/', view_medications, name='view_medications'),
        path('view_allergies/<str:patient_username>/', view_allergies, name='view_allergies'),
        ]