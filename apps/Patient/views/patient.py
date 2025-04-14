
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from apps.Patient.models.patient import Patient
# from apps.Patient.serializer.patient import PatientRegistrationSerializer
# from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import AllowAny  # Allows any user to access registration
from rest_framework.decorators import permission_classes

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.Patient.models.patient import Patient
from apps.Patient.serializer.patient import UserSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from apps.Patient.serializer.patient import PatientRegistrationSerializer
# @api_view(['GET'])
# def view_profile(pk):
#     data = Patient.objects.get(id=pk)
#     serializer = PatientRegistrationSerializer(data)
#     return Response(serializer.data)

        
# @api_view(['POST'])  # Only allows POST requests
# def registration(request):
#     serializer = PatientRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({'error': 'Invalid username or password'}, status=400)

#     user = authenticate(username=username, password=password)
#     if user:
#         # Get or create the token for the user
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'key': token.key}, status=200)
#     else:
#         return Response({'error': 'Invalid username or password'}, status=400)
    

# # Corrected view_profile for GET requests
# @api_view(['GET'])
# def view_profile(request, pk):
#     try:
#         data = Patient.objects.get(id=pk)
#         serializer = PatientRegistrationSerializer(data)
#         return Response(serializer.data)
#     except Patient.DoesNotExist:
#         return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)


# Registration should be open to all (no token needed for POST requests)
# apps/Patient/views.py

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from apps.Patient.serializer.patient import PatientRegistrationSerializer
# from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated access to the registration view
def register_patient(request):
    """
    API view to handle patient registration (creates both User and Patient).
    """
    if request.method == 'POST':
        # Initialize the serializer with the data from the request
        serializer = PatientRegistrationSerializer(data=request.data)

        # Check if the serializer data is valid
        if serializer.is_valid():
            # Create the user and patient using the serializer's create method
            patient = serializer.save()

            # Return a success response with patient details
            return Response({
                'id': patient.id,
                'user': {
                    'username': patient.user.username,
                    'first_name': patient.user.first_name,
                    'last_name': patient.user.last_name,
                    'email': patient.user.email
                },
                'phone_number': patient.phone_number,
                'date_of_birth': patient.date_of_birth,
                'current_city': patient.current_city,
                'gender': patient.gender
            }, status=HTTP_201_CREATED)

        # If serializer is not valid, return error response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    
# Login to authenticate and get token
@api_view(['POST'])
@permission_classes([AllowAny])  # This ensures the login view is accessible without authentication
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Invalid username or password'}, status=400)

    user = authenticate(username=username, password=password)
    if user:
        # Get or create the token for the user
        token, created = Token.objects.get_or_create(user=user)
        return Response({'key': token.key}, status=200)
    else:
        return Response({'error': 'Invalid username or password'}, status=400)

    
@api_view(['GET'])
def view_profile(request, pk):
    try:
        # Retrieve the patient by ID
        patient = Patient.objects.get(id=pk)
        
        # Serialize the patient data
        serializer = PatientRegistrationSerializer(patient)

        # Return the serialized data
        return Response(serializer.data)

    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)