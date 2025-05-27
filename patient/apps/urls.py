from django.urls import path

from apps.views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patient', PatientListView.as_view(), name='patient-list'),
    path('patient/<int:pk>', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create', PatientCreateView.as_view(), name='patient-create'),
    path('patient/update/<int:pk>', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/delete/<int:pk>', PatientDeleteView.as_view(), name='patient-delete'),
]
