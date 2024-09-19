from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import *
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import render

def dashboard_view(request):
    # Fetch totals
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    total_bills = Billing.objects.count()
    total_paid_bills = Billing.objects.filter(payment_status='Paid').count()
    total_unpaid_bills = Billing.objects.filter(payment_status='Pending').count()

    # Upcoming appointments (next 7 days)
    today = timezone.now().date()
    upcoming_appointments = Appointment.objects.filter(appointment_date__gte=today).order_by('appointment_date')[:5]

    # Sum of all billing amounts
    total_revenue = Billing.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    unpaid_billing_amount = Billing.objects.filter(payment_status='Pending').aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'total_bills': total_bills,
        'total_paid_bills': total_paid_bills,
        'total_unpaid_bills': total_unpaid_bills,
        'upcoming_appointments': upcoming_appointments,
        'total_revenue': total_revenue,
        'unpaid_billing_amount': unpaid_billing_amount,
    }
    
    return render(request, 'dashboard.html', context)

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'

class PatientCreateView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address']
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'email', 'address']
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    context_object_name = 'doctors'

class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'phone_number', 'email']
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialty', 'phone_number', 'email']
    template_name = 'doctors/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['patient', 'doctor', 'appointment_date', 'symptoms']
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['patient', 'doctor', 'appointment_date', 'symptoms']
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')

class BillingListView(ListView):
    model = Billing
    template_name = 'billings/billing_list.html'
    context_object_name = 'billings'

class BillingCreateView(CreateView):
    model = Billing
    fields = ['patient', 'appointment', 'total_amount', 'payment_status']
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingUpdateView(UpdateView):
    model = Billing
    fields = ['patient', 'appointment', 'total_amount', 'payment_status']
    template_name = 'billings/billing_form.html'
    success_url = reverse_lazy('billing_list')

class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'billings/billing_confirm_delete.html'
    success_url = reverse_lazy('billing_list')
