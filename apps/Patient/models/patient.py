from django.db import models



class Patient(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15, blank=True, null=True )
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F'),('Female')], blank= True, null=True)

    class Meta:
        db_table = 'patient'
        constraints = [
            models.UniqueConstraint(field=['user_name'], name='unique_user_name'),
        ]
        indexes = [
            models.Index(fields=['user_name']),
        ]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"