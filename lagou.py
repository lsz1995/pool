import json
import math
import time

import pymongo
import  requests

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
lagou = mydb['lagou1']

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.140515923.1521033456; user_trace_token=20180314211737-108f44d6-278a-11e8-b1e5-5254005c3644; LGUID=20180314211737-108f4a20-278a-11e8-b1e5-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; _gid=GA1.2.1511254984.1522590469; WEBTJ-ID=20180401214748-1628176caa2d7-0746f7ebd81c67-4446042d-1049088-1628176caa3283; LGSID=20180401214750-44ff0999-35b3-11e8-ac29-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.000000KxuWOh0sww8TlQlcfM6QLGTUHo75kFnBgVXDH3jsDw_qBYa4GWA43b9gl9dYwbRT9Dhvy54w-ekqLP4NOTFLDLP4OLCyMFxv9k8pJMpCGFBswC8QUnaQbFC3tajqFZqGfmA_VTheie1sUN2BxBN8m-UApcFGSPIJCtl4ChJXKOH6.DY_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzqAM-HgguoLt8HGLFodt8Z1lTr1dsePSZ1L3ISHjeIlhGv-5QWdQjPakg3vUnB6.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4_sKGUHYznWR0u1dBUW0s0ZNG5yF9pywd0ZKGujYd0APGujYLn0KVIjYknjDLg1DsnH-xnH0zndt1nj0zg1nvnjD0pvbqn0KzIjY1nHm0uy-b5HDYPjIxnHbsn1uxnWDknjKxnWmknjR0mhbqnW0Y0AdW5HTzrHmzP10dP7tLn10kPHf3PW-xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5HDYPWn4PHR4Pj60UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1Y4rjT3nH6dPWfdn1m3PjDsnjns0ZF-TgfqnHRznWR4njfdPjn1P6K1pyfquHNWPvRLPjRsnj0duj0zrfKWTvYqP1Tswjn3PW0vP16zrH-jn0K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nH6Lnj7xn0Ksmgwxuhk9u1Ys0AwWpyfqnWm3PjndPjRv0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HnLn6%26ck%3D7552.1.79.248.143.237.156.837%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.0.0.0%26ie%3Dutf-8%26f%3D8%26tn%3Dbaiduhome_pg%26wd%3D%25E6%258B%2589%25E9%2592%25A9%26oq%3Dlagou%26rqlang%3Dcn%26inputT%3D2233%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_xm_e110f9_265e1f_%25E6%258B%2589%25E9%2592%25A9; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521033549,1522473356,1522473567,1522590475; X_HTTP_TOKEN=52c3d4a7df25bb563eebf7134528712f; _putrc=25204D22603B44E6; JSESSIONID=ABAAABAACBHABBI10F8000F0A05F13D698BB0FE6A5BA21F; login=true; unick=%E5%88%98%E5%8A%AD%E5%93%B2; LG_LOGIN_USER_ID=06a43f7dd2a03164b7c63c642004925d855c3aed1bfb89a2; gate_login_token=2db54f8d786ba36211adf35978a65a58fdbab6d53b9f4a57; TG-TRACK-CODE=index_search; SEARCH_ID=a64e2189f9fe4345ad3db776e9060f14; LGRID=20180401215705-8fb7026a-35b4-11e8-b6d4-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522591028',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(url,params):
     html = requests.get(url,data=params,headers=headers)
     json_data = json.loads(html.text)# 转成json格式

     total_count = json_data['content']['positionResult']['totalCount']

     page_number = math.ceil(total_count/15) if math.ceil(total_count/15)<30 else 30
     get_info(url,page_number)



def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first':'true'if page == 1 else 'false',
            'pn':str(pn),
            'kd':'python'
        }
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos ={
                        'businessZones': result['businessZones'],
                        'city':result['city'],
                        'companyFullName': result['companyFullName'],
                        'companyLabelList': result['companyLabelList'],
                        'companySize': result['companySize'],
                        'district': result['district'],
                        'education': result['education'],
                        'explain': result['explain'],
                        'financeStage': result['financeStage'],
                        'firstType': result['firstType'],
                        'formatCreateTime': result['formatCreateTime'],
                        'gradeDescription': result['gradeDescription'],
                        'imState': result['imState'],
                        'industryField': result['industryField'],
                        'jobNature': result['jobNature'],
                        'positionAdvantage': result['positionAdvantage'],
                        'salary': result['salary'],
                        'secondType': result['secondType'],
                        'workYear': result['workYear']
                }
                print(infos)
                print('__________________')

                lagou.insert_one(infos)
            time.sleep(2)
        except requests.exceptions.ConnectionError:
                pass

if __name__ == "__main__":
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first':'true',
        'pn':'1',
        'kd':'python'
    }
    get_page(url,params)