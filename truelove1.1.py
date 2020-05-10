# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:53:58 2020

@author: house
"""


import re
import urllib.request



#链接
url = 'https://mall.bilibili.com/mall-c-search/blind_box/info?itemsId='
acturl = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103089'
acturl2 = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103098'
acturl3 = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103080'
acturl4 = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103073'
acturl5 = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103074'
acturl6 = 'https://show.bilibili.com/api/selection-c/index/items/cardList?taskId=103092'

#获取源码
iget = urllib.request.urlopen(acturl)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-80101
    

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()

#PPPPPPPPPPPPPPPPPPPPP
#获取源码
iget = urllib.request.urlopen(acturl2)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-40304

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()

#PPPPPPPPPPPPPPPPPP
#获取源码
iget = urllib.request.urlopen(acturl3)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-58803

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()

#PPPPPPPPPPPPPPPPPPPPP
#获取源码
iget = urllib.request.urlopen(acturl4)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-40920

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()

#PPPPPPPPPPPPPPPPPPPPPPPPPPP
#获取源码
iget = urllib.request.urlopen(acturl5)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-104395

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()

#PPPPPPPPPPPPPPPPPPPP
#获取源码
iget = urllib.request.urlopen(acturl6)
code = iget.read().decode('utf8')

#正则规则
rule = re.compile(r'itemsId=(.*?)"')
name = re.compile(r'"name":"(.*?)","itemsType"')
sales = re.compile(r'"sales":(\d+\.?\d*)')
stock = re.compile(r'"stock":(\d+\.?\d*)')

#建立list
goodsid = re.findall(rule,code)

#REM
resp0 = urllib.request.urlopen(url+goodsid[0])
resp1 = urllib.request.urlopen(url+goodsid[1])
resp2 = urllib.request.urlopen(url+goodsid[2])
resp3 = urllib.request.urlopen(url+goodsid[3])
resp4 = urllib.request.urlopen(url+goodsid[4])
resp5 = urllib.request.urlopen(url+goodsid[5])
resp6 = urllib.request.urlopen(url+goodsid[6])
resp7 = urllib.request.urlopen(url+goodsid[7])
resp8 = urllib.request.urlopen(url+goodsid[8])
resp9 = urllib.request.urlopen(url+goodsid[9])


code0 = resp0.read().decode('utf8')
code1 = resp1.read().decode('utf8')
code2 = resp2.read().decode('utf8')
code3 = resp3.read().decode('utf8')
code4 = resp4.read().decode('utf8')
code5 = resp5.read().decode('utf8')
code6 = resp6.read().decode('utf8')
code7 = resp7.read().decode('utf8')
code8 = resp8.read().decode('utf8')
code9 = resp9.read().decode('utf8')

saleslist = re.findall(sales,code0) + re.findall(sales,code1) + re.findall(sales,code2) + re.findall(sales,code3) + re.findall(sales,code4) + re.findall(sales,code5) + re.findall(sales,code6) + re.findall(sales,code7) + re.findall(sales,code8) + re.findall(sales,code9)
saleslist = [int(x) for x in saleslist]
salesum0 = 0
for i in saleslist:
    salesum0 = salesum0 + i
    salesum10 =  salesum0-148128    

stocklist = re.findall(stock,code0) + re.findall(stock,code1) + re.findall(stock,code2) + re.findall(stock,code3) + re.findall(stock,code4) + re.findall(stock,code5) + re.findall(stock,code6) + re.findall(stock,code7) + re.findall(stock,code8) + re.findall(stock,code9)
stocklist = [int(x) for x in stocklist]
stocksum0 = 0
for i in stocklist:
    stocksum0 = stocksum0 + i



print('---------------------------------------')
print(re.findall(name,code0))
print('今日累计出售:',salesum10)
print('总剩余库存:',stocksum0)

file=open('bilibili.txt','a') 
file.write(str(re.findall(name,code0))+'\n'+'今日累计出售:'+str(salesum0)+'\n'+'总剩余库存:'+str(stocksum0)+'\n'); 
file.close()