from django.shortcuts import render
from django.http import Http404
from models import Patient
from appmhistory.serializers import PatientSerializer
#from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#class PatientViewSet(ModelViewSet):
# queryset = Patient.objects.all()
# serializer_class = PatientSerializer

class PatientList(APIView):
 """ List all Patients, or create a neew Patient """
 def get(self, request, format=None):
  patients = Patient.objects.all()
  serializer = PatientSerializer(patients, many=True)
  return Response(serializer.data)
	
 def post(self, request, format=None):
  serializer = PatientSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response(serializer.data, status=status.HTTP_201_CREATED) 
  return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

 def delete(self, request, pk, format=None):
  patient = self.get_object(pk)
  patient.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

class PatientDetail(APIView):
 """ Retrieve, update, or delete a patient instance
 """

 def get_object(self, pk):
   try:
    return Patient.objects.get(pk=pk)
   except Patient.DoesNotExist:
    raise Http404
	
 def get(self, request,pk, format=None):
  patient = self.get_object(pk)
  patient = PatientSerializer(patient)
  return Response(patient.data)

 def put(self, request, pk, format=None):
  patient = self.get_object(pk)
  serializer = PatientSerializer(patient, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response(serializer.data)			
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
 def delete(self, request, pk, format=None):
  patient = self.get_object(pk)
  patient.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
	
	

