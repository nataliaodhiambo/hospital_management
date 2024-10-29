from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient, Appointment
from django.views import View
from .forms import AppointmentForm
from . import views

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

#for displaying the list of doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {'doctors' : doctors}
    return render(request, 'core/doctor_list.html', context)

#for displaying specific doctor details
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    context = {'doctor' : doctor}
    return render(request, 'core/doctor_detail.html', context)

#view list of all patients
def patient_list(request):
    patients = Patient.object.all()
    context = {'patients' : patients}
    return render(request, 'patient_list.html', context)

#view to display details of a specific patient
def patient_detail (request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    context = {'patient' : patient}
    return render (request, 'patient_detail.html', context)

#view to create a new appointment
def appointment_create(request):
    if  request.method == 'POST':
        doctor = Doctor.objects.get(pk=request.POST['doctor'])
        patient = Patient.objects.get(pk=request.POST['patient'])
        date_time = request.POST['date_time']
        reason = request.POST['reason']
        appointment = Appointment.objects.create(
        doctor=doctor, patient=patient, date_time=date_time, reason=reason)
        return redirect('appointment_detail', pk=appointment.pk) #redirect user to appointment details
    else:
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()
        context = {'doctors': doctors, 'patients': patients}
        return render(request, 'appointment_form.html', context)

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