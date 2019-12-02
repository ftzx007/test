from Credit_platform_pc.api.api_post_statusCount import ApiStatuscount
from Credit_platform_pc.tools.Read_json import read_json
from parameterized import parameterized
import unittest


def get_data():

    data = read_json('dataCount.json')
    arrs = []
    arrs.append((
                 data.get('url'),
                 data.get('headers'),
                 data.get('status_code')
                                    ))
    return arrs

class TestStatusconut(unittest.TestCase):
    def setUp(self):
        self.api = ApiStatuscount

    @parameterized.expand(get_data)
    def testStatuscount(self,url,headers,status_code):
        r = self.api.api_post_statuscount(self,url=url,headers=headers)
        print(r.json())

        try:
            self.assertEqual(status_code,r.status_code)
        except AssertionError as e:
            raise e

