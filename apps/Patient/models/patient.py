from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True) # Use Django's auth.User
    phone_number = models.CharField(max_length=15, blank=True, null=True,validators=[
        RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    ] ) # example : +1234567890
    date_of_birth = models.DateField(blank=True, null=True)
    current_city = models.CharField(max_length=20,choices=[('Amude','Amude'),('Berlin','Berlin')],blank=True, null=True)
    gender = models.CharField(max_length=1,choices=[('M', 'Male'), ('F', 'Female')],blank=True,null=True)


    class Meta:
        db_table = 'patient'
        # constraints = [           +++ this constraint does like: OneToOneField +++
        #     models.UniqueConstraint(fields=['user'], name='unique_user')# this does like
        # ]
        indexes = [
            models.Index(fields=['user']), #  index is a data structure that speeds up querying on specific fields 
        ]

    def __str__(self):
        if self.user:
            return f"{self.user.first_name} {self.user.last_name}"
        return "Unassigned Patient"
        


