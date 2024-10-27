from django.shortcuts import render, redirect
from django.views import View
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

class DoctorListView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'core/doctor_list.html', {'doctors': doctors})

class PatientListView(View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'core/patient_list.html', {'patients': patients})

class AppointmentListView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'core/appointment_list.html', {'appointments': appointments})

class AppointmentCompleteView(View):
    def post(self, request, pk):
        appointment = Appointment.objects.get(pk=pk)
        appointment.complete_appointment()
        return redirect('appointment_list')

class AppointmentCreateView(View):
    def get(self, request):
        form = AppointmentForm()
        return render(request, 'core/appointment_form.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
        return render(request, 'core/appointment_form.html', {'form': form})