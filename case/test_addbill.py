import unittest
from parameterized import parameterized
from Credit_platform_pc.api.api_post_addbill import ApiAddbill
from Credit_platform_pc.tools.Read_json import read_json

def get_data():
    data = read_json('adbill.json')
    arrs = []
    arrs.append((data.get('url'),
                 data.get('headers'),
                 data.get('data'),
                 data.get('status_code'))
        )
    return arrs

class TestAdbill(unittest.TestCase):
    def setUp(self):
        self.api = ApiAddbill

    @parameterized.expand(get_data)
    def testadbill(self,url,headers,data,status_code):
        r = self.api.api_post_addbill(self,url=url,headers=headers,data=data)

        print(r.json())
        try:
            self.assertEqual(status_code,r.status_code)
        except AssertionError as e:
            raise e


