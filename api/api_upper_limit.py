import requests

class Api_upperlimit:
    def api_post_upperlimit(self,url,headers,data):
        return requests.post(url=url,headers=headers,data=data)
