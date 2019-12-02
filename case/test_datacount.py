import unittest
from Credit_platform_pc.tools.Read_json import read_json
from parameterized import parameterized
from Credit_platform_pc.api.api_post_dataCount import ApiDatacount

def get_data():
    arrs = []
    data = read_json('checkstock.json')
    arrs.append(
        (data.get('url'),
         data.get('headers'),
         data.get('status_code'))
    )
    return arrs

class TestDatacount(unittest.TestCase):
    def setUp(self):
        self.api = ApiDatacount

    @parameterized.expand(get_data)
    def testDatacount(self,url,headers,status_code):
        r = self.api.api_post_apidatacount(self,url=url,headers=headers)
        print(r.json())

        try:
            self.assertEqual(status_code,r.status_code)
        except AssertionError as e:
            raise e

