# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:22:58 2020

@author: house
"""

#引入模块
import urllib.request
import re



activityurl = 'https://mall.bilibili.com/blackboard/activity-MK_1yNhfg.html'
resp = urllib.request.urlopen(activityurl)
code = resp.read().decode('utf8')
nmsl = re.compile(r'box_detail&noTitleBar=1&itemsId=(.*?)&from=cms_yxsjzg_mhzb')
list = list(set(re.findall(nmsl,code)))


#填写URl
url = 'https://mall.bilibili.com/mall-c-search/blind_box/info?itemsId='

#抓取网址
resp0 = urllib.request.urlopen(url+list[0])
resp1 = urllib.request.urlopen(url+list[1])
resp2 = urllib.request.urlopen(url+list[2])
resp3 = urllib.request.urlopen(url+list[3])
resp4 = urllib.request.urlopen(url+list[4])
resp5 = urllib.request.urlopen(url+list[5])


#获得源码
code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')


#来个暴力的正则
rule = re.compile(r'"sales":\d+\.?\d*,"stock":\d+\.?\d*')
name = re.compile(r'"name":"(.*?)","itemsType"')


print('-------------------------------------------------')
print(re.findall(name,code0))
print(re.findall(rule,code0))
print('-------------------------------------------------')
print(re.findall(name,code1))
print(re.findall(rule,code1))
print('-------------------------------------------------')
print(re.findall(name,code2))
print(re.findall(rule,code2))
print('-------------------------------------------------')
print(re.findall(name,code3))
print(re.findall(rule,code3))
print('-------------------------------------------------')
print(re.findall(name,code4))
print(re.findall(rule,code4))
print('-------------------------------------------------')
print(re.findall(name,code5))
print(re.findall(rule,code5))
