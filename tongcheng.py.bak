import requests
import time
import re
import pymysql  



connect = pymysql.Connect(  
    host='****',  
    port=3306,  
    user='****',  
    passwd='******',  
    db='****', 
    use_unicode=1,
    charset='utf8'  
)   
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

for url1 in url_net:
    html1 = requests.post(url1, headers = headers)
    pages = html1.json()['pageInfo']['totalPage']
    print(pages)
    urls = []

    #url1.split("page=1")
    for j in range(pages):
        url = url1.split("page=1")[0] + 'page=' + str(j) + url1.split("page=1")[1]
        #url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page='+str(j)+'&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
        urls.append(url)
    
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
            #print(k)
            #print(user,ID,jingdian,time,content)
                cursor = connect.cursor()  
                sql = "INSERT IGNORE INTO tongchen (ID, user, jingdian, time, content) VALUES ( '%s', '%s', '%s', '%s', '%s' )"  
                data = ( ID, user, jingdian, time1, content)
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
        #html1 = requests.post(urls[k], headers = headers)
        #time.sleep(3)
        #s = requests.session()
        #s.keep_alive = False
        
        
  

cursor.close()
db.close()    
    