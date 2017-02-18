from __future__ import unicode_literals
from appmhistory.models import Patient
import unittest
import six
import HTMLTestRunner


def register_Patient(name, ci, register_date):
    return Patient.objects.create(name=name, ci=ci, register_date= register_date)


class TestViews(unittest.TestCase):
    def test_PatientName_is_String(self):
        patient = register_Patient('Jhon Perez', '456', '2017-01-21')
        isPass = False
        if isinstance(patient.name, six.string_types):
            isPass = True
        self.assertTrue(isPass,"Patient name is not an instance from String")

    def test_Patient_name(self):
        patient = register_Patient('Jhon Perez1', '457', '2017-01-21')
        self.assertEqual(patient.name, 'Jhon Perez1', "Patient was created with incorrect values")

suite = unittest.TestLoader().loadTestsFromTestCase(TestViews)
unittest.TextTestRunner(verbosity=2)
output = open("resultUnitTest.html","w")
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title='Unit Test Report',
                                          description='Result Unit Test Report')
runner.run(suite)

