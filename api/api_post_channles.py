import requests

class ApiChannles:

    #请求获取工单列表
    def api_post_channle(self,url,headers):
        return requests.post(url=url,headers=headers)




