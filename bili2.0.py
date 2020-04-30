# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:20:40 2020

@author: lanmaomao
"""


import urllib.request
import requests
import re
import datetime
import time

#print('请输入第1个角色初始票数|回车键提交|单位(票):')  #无法自动获取，差评
#a = int(input())
#print('请输入第2个角色初始票数|回车键提交|单位(票):')  #不如直接设定好数值
#b = int(input())
#print('请输入第3个角色初始票数|回车键提交|单位(票):')
#c = int(input())
#print('请输入第4个角色初始票数|回车键提交|单位(票):')
#d = int(input())

a = 808  #4.29用的数据
b = 19372
c = 17957
d = 44380
sum0 = a + b + c + d #简陋的求和



    
while 1 > 0:  #简陋的循环装置
    start = time.process_time()     #计时开始
    resp=urllib.request.urlopen('https://mall.bilibili.com/mall-c-search/ip/role_protect/list?channel=bilibili140&ipId=0_3000316&type=3')
    html=resp.read() #获取源码
    Source_code = html.decode('utf8') #简陋的转化编码
    
    rule1 = re.compile(r'2100307,"hotPower":{"hotPower":(.*?),"') #简陋的正则匹配
    rule2 = re.compile(r'2100526,"hotPower":{"hotPower":(.*?),"') #用一天改一天
    rule3 = re.compile(r'64504,"hotPower":{"hotPower":(.*?),"')
    rule4 = re.compile(r'2100530,"hotPower":{"hotPower":(.*?),"')


    vote = re.findall(rule1,Source_code) + re.findall(rule2,Source_code) + re.findall(rule3,Source_code) + re.findall(rule4,Source_code)
        
    vote = [int(x) for x in vote] #字符串转化为整数

    sum = 0 #简陋的求和
    for i in vote:
        sum = sum + i
        
    sum1 = sum -sum0

    votes1 = vote[0]-a
    votes2 = vote[1]-b
    votes3 = vote[2]-c
    votes4 = vote[3]-d
    
    vote1 = round(votes1/sum1*100) #应投喂饼干数量
    vote2 = round(votes2/sum1*100) #简陋的算法
    vote3 = round(votes3/sum1*100)
    vote4 = round(votes4/sum1*100)
    
    list = [votes1,votes2,votes3,votes4]
    
    print("--------------------")
    print('本周获得爱心值',vote)
    print('今日获得爱心值',list)
    print("--------------------")
    print('角色1应投喂:',vote1)
    print('角色2应投喂:',vote2)
    print('角色3应投喂:',vote3)
    print('角色4应投喂:',vote4)
    print("----------")
    print('当前时间:',datetime.datetime.now()) #显示时间，好像没什么用



    headers = {
        
        'Cookie':'_uuid=0C2C7110-B7CA-777A-F5C9-3A01FFCA942496887infoc;buvid3=74776370-0B30-4278-A37F-F381D3B6D29A53926infoc; sid=bi4joh87; DedeUserID=215309448;DedeUserID__ckMd5=28297a6810e002cb;SESSDATA=d2bc0e0c%2C1603528068%2C8b494*41;bili_jct=96dd38433065dcf4e93573230a8e00ee',
        'Host':'show.bilibili.com',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36'
            }

    url = 'https://show.bilibili.com/api/activity/index/iprank/vote'
    postdata={"taskId":"bt-tp-05","numList":
              [{"optionId":149,"num":vote1},        #POST投喂，这边得每天手动改optionId
               {"optionId":150,"num":vote2},
               {"optionId":151,"num":vote3},
               {"optionId":152,"num":vote4}],
              "activityId":"bt20-tp"}
    
    end = time.process_time()       #计时结束

    print('计算共耗时: %6.3f 秒\n\n' % (end - start))     #输出时间

    r=requests.post(url,headers = headers,json=postdata)

    print(r.text)

    time.sleep(1) #停止5秒(当上面的while注释掉之后这里没有什么用处)
