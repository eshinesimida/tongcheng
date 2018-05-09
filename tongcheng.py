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
#url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page=2&pageSize=10&labId=1&sort=0&iid=0.7615521549189274'
#url1= 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page=1&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
url_net = [
        #'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=19466&page=1&pageSize=10&labId=6&sort=0&iid=0.6362413561168098',
        #'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=18007&page=1&pageSize=10&labId=6&sort=0&iid=0.04777261337970473',
        #'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=12851&page=1&pageSize=10&labId=6&sort=0&iid=0.6255524150197138'
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=18738&page=1&pageSize=10&labId=6&sort=0&iid=0.7897820373766561',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=4510&page=1&pageSize=10&labId=6&sort=0&iid=0.42065800212812665',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=8109&page=1&pageSize=10&labId=6&sort=0&iid=0.9786362329833097',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=24621&page=1&pageSize=10&labId=6&sort=0&iid=0.8709899592908121',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=4037&page=1&pageSize=10&labId=6&sort=0&iid=0.0895729115312871',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=27448&page=1&pageSize=10&labId=6&sort=0&iid=0.7115398973537116',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=19501&page=1&pageSize=10&labId=6&sort=0&iid=0.9287208744417104',
        'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3387&page=1&pageSize=10&labId=6&sort=0&iid=0.671316653986964'

        ]
for url1 in url_net:
    html1 = requests.post(url1)
    pages = html1.json()['pageInfo']['totalPage']
    print(pages)
    urls = []

    #url1.split("page=1")
    for j in range(pages):
        url = url1.split("page=1")[0] + 'page=' + str(j) + url1.split("page=1")[1]
        #url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page='+str(j)+'&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
        urls.append(url)
    
    for k in range(pages):
        html1 = requests.post(urls[k])
        time.sleep(3)
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
        
  

cursor.close()
db.close() 
    
    
    