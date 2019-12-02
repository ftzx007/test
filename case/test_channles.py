import unittest
from parameterized import parameterized
from Credit_platform_pc.api.api_post_channles import ApiChannles
from Credit_platform_pc.tools.Read_json import read_json

def get_data():
    data = read_json("channels.json")
    arrs = []
    arrs.append((data.get('url_Channles'),
                 data.get('hearders'),
                 data.get('status_code'),
                 data.get('except_result')
                 ))

    return arrs

class TestChannles(unittest.TestCase):

    def setUp(self):
        # self.url_Channles = 'http://118.190.207.192:9133/index/rbac/getMenuFunc'
        # self.heards = {'Content-Type': 'applicaion/json',
        #           'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NzIzMzg3NjQsImV4cCI6MTU3NDkzMDc2NCwiZGF0YSI6eyJ1aWQiOjEsImNvbXBhbnlfaWQiOjF9fQ.W1ZCrN1_D-pwLgeTVxbIILodBNBU5w2nX4K1j1cXYcQ'}
        self.api = ApiChannles()

    @parameterized.expand(get_data)
    def test_post_channels(self,url_Channles,headers,status_code,expect_result):
        r = self.api.api_post_channle(url=url_Channles,headers=headers)
        try:
            self.assertEqual(status_code,r.status_code)

            self.assertEqual(expect_result,r.json()['msg'])

        except AssertionError as e:
            print(e)

if __name__ == '__main__':
    unittest.main()

