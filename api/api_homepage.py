import requests

class ApiHomepage:
    def api_post_homepage(self,url,headers):
        return requests.post(url=url,headers=headers)
