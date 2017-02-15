import unittest
import requests
import xmlrunner

class TestViews(unittest.TestCase):
    def setUp(self):
        self.command = 'curl'
        self.server = 'http://127.0.0.1'
        self.port = '8000'
        self.application_name = '/appmhistory'
        print('Init test')

    def test_request_POST(self):
        res = requests.post(self.server + ':' + self.port + self.application_name + '/', headers='', data= {'name':'Maria Perez', 'ci':'451','register_date':'2017-01-13'})
        self.assertTrue(res.status_code == 201)

    def test_request_GET(self):
        res = requests.get(self.server + ':' + self.port + self.application_name + '/', headers='')
        self.assertTrue(res.status_code == 200)

if __name__ == '__main__':
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
