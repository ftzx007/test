import unittest
from parameterized import parameterized
from Credit_platform_pc.tools.Read_json import read_json
from Credit_platform_pc.api.api_homepage import ApiHomepage

def get_data():
    data = read_json('homepage.json')
    arrs = []
    arrs.append((data.get('url'),
                 data.get('headers'),
                data.get('status_code'),
                data.get('expect_result'),))


    return arrs

class TestHomepage(unittest.TestCase):
    def setUp(self):
        self.api = ApiHomepage
    @parameterized.expand(get_data)
    def test_hompage(self,url,headers,status_code,expect_result):
        r = self.api.api_post_homepage(self,url=url,headers=headers)
        print(r.json())
        try:
            self.assertEqual(status_code,r.status_code)
        except AssertionError as e:
            raise e




