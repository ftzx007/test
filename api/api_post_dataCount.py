#按日统计工单状态（折线图）接口
import requests

class ApiDatacount:

    def api_post_apidatacount(self,url,headers):
        return requests.post(url=url,headers=headers)