import requests

class ApiStatuscount:
    def api_post_statuscount(self,url,headers):
        return requests.post(url=url,headers=headers)