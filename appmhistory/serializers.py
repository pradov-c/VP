from django.forms import widgets
from rest_framework import serializers
from appmhistory.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('ci', 'name', 'register_date')

    def create(self, validated_data):
        """
        Create and return a new Patient instance, given the validate data
        :param validated_data:
        :return:
        """
        return Patient.objects.create(**validated_data)

    def update(self, instance, validate_data):
        """
        Update and return an existing Patient instance, given the validate data.
        :param instance:
        :param validate_data:
        :return:
        """
        instance.name = validate_data.get('name', instance.title)
        instance.register_date = validate_data.get('validate_date', instance.register_date)
        instance.ci = validate_data.get('ci', instance.ci)
        instance.save()
        return instance
