#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#by i3ekr

import re,optparse,sys,requests,time,os

parse = optparse.OptionParser(usage="python %prog -i '127.0.0.1'",version="%prog 1.0")
parse.add_option('-i','--ip',action='store',dest='ip',help='ip parse...')
parse.add_option('-o','--out',action='store',dest='out',help='this parse is out result file exp:-o "/tmp/result.txt""')
parse.set_defaults(v=1.2)
options,args=parse.parse_args()


def gethtml(ip,page):
    try:
        html = requests.get("https://www.bing.com/search?q=ip:"+ip+"&qs=ds&first="+str(page)+"&FORM=PERE4").content
        return html
    except Exception as e:
        return "访问错误"
        exit()

def chongfu():
    with open("./tmp.txt","r") as f:
        tmp = f.read()
        url = tmp.split("\r\n")
        for i in set(url):
            with open("ok.txt","a") as f:
                f.write(i+'\r\n')

def geturl(html):
    try:
        url = re.findall(r"(?<=<cite>).*?(?=</cite>)", html)
        print (url)
        for u in url:
            with open("./tmp.txt","a") as f:
                f.write(u+"\r\n")
                f.close()
    except Exception as e:
        raise e

#根据索引出来的搜索量来判断有多少个页面，返回值是页面数量
def result_page():
    try:
        num = str(re.findall(r"<span class=\"sb_count\">(.*?)</span><span class=\"ftrB\"",html)[0]).strip(" 条结果")
        page = int(num.replace(",",""))
        return page/10
    except Exception as e:
        print ("没有与此相关的结果")
        exit()




if __name__ == "__main__":
    # print """
    #         =========================
    #         [+] by i3ekr
    #         [+] Blog nul1.cnblogs.com
    #         [+] Time 2018/6/13
    #         =========================
    # """
    if len(sys.argv) > 2:
        url_pangzhan = []
        pg = 1
        ip = options.ip
        f = False
        while True:
            if f == False:
                html = requests.get("https://www.bing.com/search?q=ip:"+ip+"&qs=ds&first=1&FORM=PERE4").content
                result_page()
                f = True
            else:
                for i in xrange(0,result_page()):
                    html = gethtml(ip,pg)
                    url = geturl(html)
                    print ("第[%s]页"%(i+1))
                    pg+=11

                chongfu()
                os.remove('tmp.txt')
                exit()

    else:
        print(options.usage())
        exit()