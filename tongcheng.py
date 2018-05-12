from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
import requests
from DAO.xiecheng import xiechengDAO
import random
import pymysql


connect = pymysql.Connect(
    host='****',
    port=3306,
    user='****',
    passwd='****',
    db='*****',
    use_unicode=1,
    charset='utf8'
)
class XiechenghotelService(object):

    def __init__(self):
        
        self.xiechengDao = xiechengDAO()
      
        self.hotelItem = {}
        
        self.commList = []


    
    def getdata(self):

        Lianjie_data = self.xiechengDao._return()
        for lianjie_data in Lianjie_data:
            self.intohotel(lianjie_data[7])




    def intohotel(self,Links):

        url = Links
        print url
        print url.split("page=1")[0],url.split("page=1")[1]

      

        headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

       
        html1 = requests.post(url, headers=headers)
        pages = html1.json()['pageInfo']['totalPage']
        print pages
        urls = []


        for j in range(pages):
            url1 = url.split("page=1")[0] + 'page=' + str(j) + url.split("page=1")[1]
            print j
            # url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page='+str(j)+'&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
            urls.append(url1)

        for k in range(pages):
            try:
                html1 = requests.post(urls[k], headers=headers, timeout=5)

                for i in range(10):
                    content = html1.json()['dpList'][i]['dpContent']
                    content = re.sub(r"'", "", content)
                    time1 = html1.json()['dpList'][i]['dpDate']
                    jingdian = html1.json()['dpList'][i]['DPItemName']
                    user = html1.json()['dpList'][i]['dpUserName']
                    ID = html1.json()['dpList'][i]['dpId']
                        # print(k)
                        # print(user,ID,jingdian,time,content)
                    cursor = connect.cursor()
                    sql = "INSERT IGNORE INTO tongchen (ID, user, jingdian, time, content) VALUES ( '%s', '%s', '%s', '%s', '%s' )"
                    data = (ID, user, jingdian, time1, content)
                    try:
                        cursor.execute(sql % data)
                    except:
                        print(ID)

                    connect.commit()
                print(k)
                print(jingdian)
            except requests.exceptions.ConnectionError as e:
                html1 = "No response"
                continue

    

if __name__=="__main__":
    xiechenghotelService = XiechenghotelService()
    xiechenghotelService.getdata()
    