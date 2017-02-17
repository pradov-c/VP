# -*- coding: utf-8 -*-
import requests
from behave import given, when, step, then, use_step_matcher
import os

test_server = os.environ.get('TEST_SERVER', None)
test_port = os.environ.get('TEST_PORT', None)
application_name = os.environ.get('APPLICATION_NAME', None)



@given("""service is up""")
def service_up(context):
    print ('service up')
    pass


@when("""I make a Post request to register a Patient with {patientci}, {namepatient} and {registerdate}""")
def set_information_patient(context, patientci, patientname, registerdate):
    """
    Specify the patientci, patientname and registerdater in order to register a patient
    """
    stepPass = True
    context.res = requests.post(test_server + ':' + test_port + application_name  + '/', headers='', data= "{'name': '"+ patientname +"', 'ci': '"+patientci+",'register_date': '"+registerdate)
    if(context.res is None):
        stepPass = False
    assert stepPass is True

@then("""HTTP {statuscode} is returned""")
def get_statusCode_request(context):
    print('es '+context.res.status_code)
    assert context.res.status_code == int(statuscode)