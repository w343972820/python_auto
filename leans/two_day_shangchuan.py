#coding=utf-8
import requests
import json
#网站要求的文件数据格式，可忽略掉type字段
file={
    "fileField":("qwer.jpg",open("E:/vico/qwer.jpg",'rb'),"image/jpg"),
    "type":"1"
}
url='https://www.imooc.com/user/postpic'
#设置cookies信息，这里知道只需要apsid就能识别到登录信息
cookie={
    "apsid":"ZmYzJjZDU5ZWFlZmQyZTBlZmUwMmE5ZTU2OTU1OWEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOTYxOTcxNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADZkZDE4MDlkMGE2NGYwMmJhM2M2YzI5ZTAyYmJiY2E5V2b9X1dm%2FV8%3DMW",
}
#上传图片到云服务器
results_res=requests.post(url,files=file,cookies=cookie,verify=False).json()
print(results_res)
sure_url='https://www.imooc.com/user/ajaxsetportrait'
datas={
    'portrait':'5ffd71b0000157f207200500'
}
#替换上传的图片
results_tou=requests.post(sure_url,datas,cookies=cookie,verify=False).json()
print(results_tou)