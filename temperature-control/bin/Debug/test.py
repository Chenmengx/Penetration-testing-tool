#coding=utf-8
import requests
import json

url = input("请输入要识别的url地址:").encode("gbk")

def what_cms(url):
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    post={
        'hash':'0eca8914342fc63f5a2ef5246b7a3b14_7289fd8cf7f420f594ac165e475f1479',
        'url':url,
    }
    r = requests.post(url='http://whatweb.bugscaner.com/what/', data=post, headers=headers)
    # print(r)
    # r=r.content.decode("utf-8")
    print(r)
    dic = json.loads(r.text)

    if dic['cms']=='':
        return u'未识别'
    else:
        return dic['cms']


# url=str("http://www.baidu.com", "utf-8").encode("gbk")
# url = 'http://www.baidu.com'
print(what_cms(url))

