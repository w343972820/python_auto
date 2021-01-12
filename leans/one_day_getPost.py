import requests
import json
post_url='http://www.imooc.com/api3/getcourseintro'
get_url='https://www.imooc.com/course/list'
data={
   'cid':'9',
    'timestamp':'1610437559114',
    'uid':'0',
    'secrect':'',
    'uuid':'',
    'token':'c96b19a0034f7898e7260802eaf02e27'
}
#print(data)
#如果是https则需要证书，verify=False为忽略掉证书,get跟post一样
getResults=requests.get(get_url,verify=False).text
#test解析成asci码,转成json中文则会被解析
#results=requests.post(post_url,data).text
results_json=requests.post(post_url,data,verify=False).json()
#jumps为序列化格式，默认asc码，indent为缩进４格
print(json.dumps(results_json,indent=4,ensure_ascii=False))




#print(results_json)
print("it's test")