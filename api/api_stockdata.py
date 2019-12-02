import requests

class ApiStockdata:
    def api_post_stockdata(self,url,headers):
        return requests.post(url=url,headers=headers)