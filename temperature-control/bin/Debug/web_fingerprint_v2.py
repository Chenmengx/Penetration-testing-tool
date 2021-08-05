import requests
import zlib
import json
import sys


def whatweb(url):
    response = requests.get(url, verify=False)
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go", files=data)


if __name__ == '__main__':
    # request = whatweb("http://whatweb.bugscaner.com/apidoc.html")
    request = whatweb(sys.argv[1])
    # print(u"今日识别剩余次数")
    # print(request.headers["X-RateLimit-Remaining"])
    y = request.json()
    print(u"识别结果:")
    try:
        print("CMS:", y['CMS'] )
    except:
        print("CMS:未识别")
    try:
        print("Programming Languages:", y['Programming Languages'])
    except:
        print("Programming Languages:未识别")
    try:
        print("JavaScript Frameworks:", y['JavaScript Frameworks'])
    except:
        print("JavaScript Frameworks:未识别")
    try:
        print("CDN:", y['CDN'])
    except:
        print("CDN:未识别")
    try:
        print("Advertising Networks", y['Advertising Networks'])
    except:
        print("Advertising Networks:未识别")
    try:
        print("Web Servers", y['Web Servers'])
    except:
        print("Web Servers:未识别")
