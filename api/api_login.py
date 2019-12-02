'''封装接口，方法'''

import requests
class ApiWeibao:
    # #请求登录
    # def __init__(self,session):
    #     self.session = session
    def api_post_login(self,username,pwd):
        url_login = 'http://118.190.207.192:9133/index/login/loginIn'
        data = {'username': username,
                'pass': pwd}
        r = requests.post(url_login,data=data)
        return r


    def api_post_addemployee(self,name,tel,code):
        url_addemployee = 'http://118.190.207.192:9133/index/staff/add'
        data = {'name':name,
                'tel':tel,
                'code':code}
        s = requests.post(url_addemployee,data=data)

 




