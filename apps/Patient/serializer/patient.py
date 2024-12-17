# from rest_framework import serializers
# from apps.Patient.models import Patient
# from django.contrib.auth.models import User
# from apps.User.serializer.user import UserSerializer


# class PatientRegistrationSerializer(serializers.ModelSerializer):
#     # Declare user-related fields as a nested dictionary
#     user = UserSerializer()

#     class Meta:
#         model = Patient
#         fields = ['id','user','phone_number','date_of_birth','current_city','gender']



#     def create(self, validated_data):
#         # pop extract 'user' data from validated_data(data in fields ('id','user'...)) 
#         # and gives you just the user data ('username', 'password', 'first_name', 'last_name', 'email') 
#         # so you can use 'user'  somewhere else..we use it in next line
#         user_data = validated_data.pop('user') 

#         # Creating the Patient's User Account
#         user = User.objects.create_user(   
#             username=user_data['username'], # [] mean field is required
#             password=user_data['password'],
#             first_name=user_data.get('first_name', ''),
#             last_name=user_data.get('last_name', ''),
#             email=user_data.get('email', '')
        
#         )
    
    
#         # and here we add other infos to patient, we cant add this fields to user.
#         patient = Patient.objects.create(
#         user=user,
#         phone_number=validated_data.get('phone_number'),
#         date_of_birth =validated_data.get('date_of_birth'),
#         current_city = validated_data.get('current_city'),
#         gender=validated_data.get('gender')
#         )
    

        
#         return patient




#####################

# apps/User/serializer/user.py

# apps/User/serializer/user.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from apps.Patient.models import Patient
from apps.User.serializer.user import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', '')
        )
        return user


class PatientRegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'user', 'phone_number', 'date_of_birth', 'current_city', 'gender']

    def create(self, validated_data):
        # Extract the user data from the validated data
        user_data = validated_data.pop('user')

        # Create the User instance
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            email=user_data.get('email', '')
        )

        # Create the Patient instance and associate it with the created User
        patient = Patient.objects.create(
            user=user,
            phone_number=validated_data.get('phone_number'),
            date_of_birth=validated_data.get('date_of_birth'),
            current_city=validated_data.get('current_city'),
            gender=validated_data.get('gender')
        )

        return patient
