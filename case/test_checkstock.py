import unittest
from parameterized import parameterized
from Credit_platform_pc.api.api_post_checkstock import Apicheckstock
from Credit_platform_pc.tools.Read_json import read_json

def get_data():
    data = read_json('checkstock.json')
    arrs = []
    arrs.append(
        (data.get('url'),
         data.get('headers'),
         data.get('data'),
         data.get('status_code'))
    )
    return arrs
class TestCheakstock(unittest.TestCase):
    def setUp(self):
        self.api = Apicheckstock

    @parameterized.expand(get_data)
    def testCheakstock(self,url,headers,data,status_code):
        r = self.api.api_post_checkstock(self,url=url,headers=headers,data=data)
        print(r.json())

        try:
            self.assertEqual(status_code,r.status_code)

        except AssertionError as e:
            raise e
