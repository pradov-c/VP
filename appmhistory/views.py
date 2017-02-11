from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from appmhistory.models import Patient
from appmhistory.serializers import PatientSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def patient_list(request, format=None):
    """
    List all code Patient, or create a new patient.
    """
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, ci, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        patient = Patient.objects.get(ci=ci)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

