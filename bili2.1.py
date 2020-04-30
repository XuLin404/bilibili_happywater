# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:20:40 2020

@author: lanmaomao
"""

#引入模块
import urllib.request
import requests
import re
import datetime
import time
import math

#为了方便提前设置数值
a = 2197096  
b = 242951
c = 796090
d = 20391

#也可以通过键盘输入，但是我觉得太麻烦了
#print('请输入第1个角色初始票数|回车键提交|单位(票):')  #通过键盘输入数值
#a = int(input())
#print('请输入第2个角色初始票数|回车键提交|单位(票):')
#b = int(input())
#print('请输入第3个角色初始票数|回车键提交|单位(票):')
#c = int(input())
#print('请输入第4个角色初始票数|回车键提交|单位(票):')
#d = int(input())

sum0 = a + b + c + d #算出今日初始总票数


while 1 > 0:  #用一个简陋的循环来保证脚本重复运行
    start = time.process_time()     #计算程序运行所需时间|插个眼
    
    resp=urllib.request.urlopen('https://mall.bilibili.com/mall-c-search/ip/role_protect/list?channel=bilibili140&ipId=0_3000143&type=3')
    #填入要抓取源码的网址

    html=resp.read() #获取网页源码
    Source_code = html.decode('utf8') #转化一下编码
    
    rule1 = re.compile(r'16387,"hotPower":{"hotPower":(.*?),"')    #设置一个正则匹配的规则，用于筛选出所要数据
    rule2 = re.compile(r'29631,"hotPower":{"hotPower":(.*?),"')
    rule3 = re.compile(r'22430,"hotPower":{"hotPower":(.*?),"')
    rule4 = re.compile(r'27227,"hotPower":{"hotPower":(.*?),"')

    vote = re.findall(rule1,Source_code) + re.findall(rule2,Source_code) + re.findall(rule3,Source_code) + re.findall(rule4,Source_code)
    #创建一个数组
    
    vote = [int(x) for x in vote] #因为匹配出来的都是字符串类型，字符串转化为整数

    sum = 0
    for i in vote:
        sum = sum + i   #算出本周总票数|代码百度上抄的，具体意义没细看
        
    sum1 = sum -sum0    #简单算出今日总得票数

    votes1 = vote[0]-a    #算出今日单角色得票数
    votes2 = vote[1]-b
    votes3 = vote[2]-c
    votes4 = vote[3]-d
    
    vote1 = math.floor(votes1/sum1*100) #计算出应投喂饼干数量，向下取整
    vote2 = math.floor(votes2/sum1*100) #简陋的算法，但是很好用
    vote3 = math.floor(votes3/sum1*100)
    vote4 = math.floor(votes4/sum1*100)
    
    
    #从这开始是打印出数据到控制台方便查看
    list = [votes1,votes2,votes3,votes4]
    list2 = [a,b,c,d]
    
    print("--------------------")
    print('本周获得爱心值',vote)
    print('今日初始爱心值',list2)
    print('今日获得爱心值',list)
    print("--------------------")
    print('角色1应投喂:',vote1)
    print('角色2应投喂:',vote2)
    print('角色3应投喂:',vote3)
    print('角色4应投喂:',vote4)
    print("----------")
    print('当前时间:',datetime.datetime.now()) #显示时间，好像没什么用
    #打印结束

    #让我们来设置一个简单的头部用于POST提交
    headers = {
        
        'Cookie':'填入cookie要不然没法用',
        'Host':'show.bilibili.com',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Mobile Safari/537.36'
            }

    url = 'https://show.bilibili.com/api/activity/index/iprank/vote'    #设置要POST的网址
    
    postdata={"taskId":"bt-tp-06","numList":        #POST投喂，这边得每天手动改optionId
              [{"optionId":153,"num":vote1},
               {"optionId":154,"num":vote2},
               {"optionId":155,"num":vote3},
               {"optionId":156,"num":vote4}],
              "activityId":"bt20-tp"}
    
    end = time.process_time()       #计算程序运行所需时间|插个眼

    print('计算共耗时: %6.3f 秒\n\n' % (end - start))     #输出运行上述代码所需时间时间

    r=requests.post(url,headers = headers,json=postdata)    #POTS提交

    print(r.text)    #返回提交结果

    time.sleep(0.5) #暂停X秒(当上面的while注释掉之后这里没有什么用处)
