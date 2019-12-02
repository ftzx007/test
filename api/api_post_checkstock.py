import requests

class Apicheckstock:

    def api_post_checkstock(self,url,headers,data):
        return requests.post(url=url,headers=headers,data=data)