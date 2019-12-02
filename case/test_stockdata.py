import unittest

from parameterized import parameterized
from Credit_platform_pc.tools.Read_json import read_json
from Credit_platform_pc.api.api_stockdata import ApiStockdata
#数据
def get_data():
    data = read_json('stockdata.json')
    arrs = []
    arrs.append(
                (data.get('url'),
                 data.get('headers'),
                 data.get('status_code')))

    return arrs

class TestStockdata(unittest.TestCase):

    def setUp(self):
        self.api = ApiStockdata

    @parameterized.expand(get_data)
    def test_stockdata(self,url,headers,status_code):
        r = self.api.api_post_stockdata(self,url=url,headers=headers)
        print(r.json())

        try:
            self.assertEqual(status_code,r.status_code)
        except AssertionError as e:
            raise e


