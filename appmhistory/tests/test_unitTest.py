from __future__ import unicode_literals
from appmhistory.models import Patient
import unittest
import xmlrunner
import six

def register_Patient(name, ci, register_date):
    return Patient.objects.create(name=name, ci=ci, register_date= register_date)


class TestViews(unittest.TestCase):
    def test_PatientName_is_String(self):
        self.patient = register_Patient('Jhon Perez', '456', '2017-01-21')
        isPass = False
        if isinstance(self.patient.name, six.string_types):
            isPass = True
        self.assertTrue(isPass)

    def test_Patient_name(self):
        self.patient = register_Patient('Jhon Perez1', '457', '2017-01-21')
        self.assertEqual(self.patient.name, 'Jhon Perez1')

if __name__ == '__main__':
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
