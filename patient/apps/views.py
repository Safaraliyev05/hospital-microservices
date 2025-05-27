from drf_spectacular.views import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView

from apps.models import Patient
from apps.serializers import PatientSerializer


@extend_schema(tags=['Patient List'])
class PatientListView(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema(tags=['Patient Detail'])
class PatientDetailView(RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema(tags=['Patient Update'])
class PatientUpdateView(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema(tags=['Patient Create'])
class PatientCreateView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@extend_schema(tags=['Patient Delete'])
class PatientDeleteView(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
