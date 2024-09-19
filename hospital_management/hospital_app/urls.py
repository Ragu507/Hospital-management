from django.urls import path
from .views import (
    PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    AppointmentListView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,
    BillingListView, BillingCreateView, BillingUpdateView, BillingDeleteView, dashboard_view
)

urlpatterns = [
    # Patient URLs
    path('',dashboard_view,name='dashboard'),
    
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient_create'),
    path('patients/update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),

    # Doctor URLs
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),

    # Appointment URLs
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/update/<int:pk>/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/delete/<int:pk>/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    # Billing URLs
    path('billings/', BillingListView.as_view(), name='billing_list'),
    path('billings/create/', BillingCreateView.as_view(), name='billing_create'),
    path('billings/update/<int:pk>/', BillingUpdateView.as_view(), name='billing_update'),
    path('billings/delete/<int:pk>/', BillingDeleteView.as_view(), name='billing_delete'),
]
