import requests
import time
import re
#url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page=2&pageSize=10&labId=1&sort=0&iid=0.7615521549189274'
url1= 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page=1&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
url2= 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=19466&page=1&pageSize=10&labId=6&sort=0&iid=0.6362413561168098'
url3 = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=18007&page=1&pageSize=10&labId=6&sort=0&iid=0.04777261337970473'
url4 = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=12851&page=1&pageSize=10&labId=6&sort=0&iid=0.6255524150197138'
pages = html1.json()['pageInfo']['totalPage']
urls = []
for j in range(pages):
    url = 'https://www.ly.com/scenery/AjaxHelper/DianPingAjax.aspx?action=GetDianPingList&sid=3556&page='+str(j)+'&pageSize=10&labId=6&sort=0&iid=0.2556579820259157'
    urls.append(url)
#html1.json()['pageInfo']['totalPage']
#html1.json()['dpList'][2]['dpContent']
#html1.json()['dpList'][1]['dpDate']
#html1.json()['dpList'][1]['DPItemName']
#html1.json()['dpList'][1]['dpUserName']
#html1.json()['dpList'][1]['dpId']
       
#while True:
import pymysql    
db = MySQLdb.connect(host = 'rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',user = 'root',password= 'zd45+3=48', db = 'ctrip_gengxin' ,use_unicode=1,charset='utf8')
cursor = db.cursor()

connect = pymysql.Connect(  
    host='rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',  
    port=3306,  
    user='root',  
    passwd='zd45+3=48',  
    db='ctrip_gengxin', 
    use_unicode=1,
    charset='utf8'  
)  
for k in range(164,pages):
    
    #time.sleep(3)
    html1 = requests.post(urls[k])
    
    
    for i in range(10):
        content = html1.json()['dpList'][i]['dpContent']
        content = re.sub(r"'", "", content)
        time = html1.json()['dpList'][i]['dpDate']
        jingdian = html1.json()['dpList'][i]['DPItemName']
        user = html1.json()['dpList'][i]['dpUserName']
        ID = html1.json()['dpList'][i]['dpId']
        print(k)
        #print(user,ID,jingdian,time,content)
        cursor = connect.cursor()  
  
  
        sql = "INSERT IGNORE INTO tongchen (ID, user, jingdian, time, content) VALUES ( '%s', '%s', '%s', '%s', '%s' )"  
        data = ( ID, user, jingdian, time, content)
        try:
            cursor.execute(sql % data)
        except:
            print(ID)
                
        connect.commit()
        
  
        
    
import pymysql    
db = MySQLdb.connect(host = 'rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',user = 'root',password= 'zd45+3=48', db = 'ctrip_gengxin' ,use_unicode=1,charset='utf8')
cursor = db.cursor()

connect = pymysql.Connect(  
    host='rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',  
    port=3306,  
    user='root',  
    passwd='zd45+3=48',  
    db='ctrip_gengxin', 
    use_unicode=1,
    charset='utf8'  
)  
  


cursor.close()
db.close() 
    
    
    