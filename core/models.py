from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        abstract = True

class Doctor(Person):
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='doctor_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='doctor_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialty})"

class Patient(Person):
    date_of_birth = models.DateField()
    medical_history = models.TextField()

    groups=models.ManyToManyField(
        'auth.Group',
        related_name='patient_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='patient_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateField()
    reason = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient} with Dr. {self.doctor} on {self.date_time}"

    def complete_appointment(self):
        self.is_completed = True
        self.save()    