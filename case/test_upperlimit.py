from Credit_platform_pc.api.api_upper_limit import Api_upperlimit
import unittest
from parameterized import parameterized
from Credit_platform_pc.tools.Read_json import read_json


def get_data():
    data = read_json('upperlimit.json')
    arrs = []
    arrs.append((data.get('url'),
                 data.get('headers'),
                 data.get('data'),
                 data.get('expect_result'),))

    return(arrs)

class TestUpperlimit(unittest.TestCase):
    def setUp(self):
        self.url = 'http://118.190.207.192:9133/index/Stock/setTop'
        self.data = {"id":"1",
                     "stock_top":"10"}
        self.headers = {"Content_Type":"application/x_www-form_urlencoded",
                        "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzQ2NTE0OTEsImV4cCI6MTU3NzI0MzQ5MSwiZGF0YSI6eyJ1aWQiOjEsImNvbXBhbnlfaWQiOjF9fQ.5yO92h5btLpSbYD3FqXrwYn3ZboGl2C8togQCvjthGk"}
        self.api = Api_upperlimit
    @parameterized.expand(get_data)
    def test_upperlimit(self,url,headers,data,expect_result):
        try:
            r = self.api.api_post_upperlimit(self,url=url,headers=headers,      data=data)
            print(r.json())
            self.assertEqual(expect_result,r.json()['msg'])
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    unittest.main()
