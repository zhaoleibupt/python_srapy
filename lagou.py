# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:21:13 2016

@author: admin
"""
import urllib
import requests
import json

i =1
url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC'
headers = {'Host':'www.lagou.com',
           'Origin':'http://www.lagou.com',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36}',
           'Referer':'http://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%8C%97%E4%BA%AC'
          }
f =open('lagou.txt','w+')
titles = ['companyName','companySize','industryField','positionName','workYear','education','salary']
for name in titles:
   f.write(name+' ')
f.write('\n')

for i in range(1,31):
    data ={'first':'true', 'pn':str(i), 'kd':'python'}
    data=urllib.urlencode(data)
    wb_data = requests.post(url, headers = headers ,data = data)
    
    lagou = json.loads(wb_data.content)
   
    for i in range(15):
        for title in titles:
            f.write(lagou['content']['result'][i][title].encode('utf8')+';'),
        f.write('\n')
f.close()
    





 

    