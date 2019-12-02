import requests


class ApiAddbill:
    def api_post_addbill(self,url,headers,data):
        return requests.post(url=url,headers=headers,data=data)
