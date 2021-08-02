# conding=utf-8
import sys
import math  # 向上取整 math.ceil()
import threading
import requests


# 给每个线程分任务(字典中大列表分成小列表)
def muti_scan(url, threads, dic):
    with open(dic, "r") as f:
        # 读取字典文件
        dic_list = f.readlines()
        # 确定每个线程读取的行数向上取整
        thread_read_line_num = math.ceil(len(dic_list) / int(threads))
        # 制作每一个线程读取的字典列表[[t1],[t2],[t3]]
        i = 0
        result_list = []
        temp_list = []
        for line in dic_list:
            i = i + 1
            # 每一次读取到取余为零就是一个新线程任务的开始
            if i % thread_read_line_num == 0:
                temp_list.append(line.strip())
                result_list.append(temp_list)
                temp_list = []
            else:
                temp_list.append(line.strip())

    # 线程执行
    threads_list = []
    for i in result_list:
        # 创建thread类
        # 传入的参数是大列表result_list中的每一个小列表
        threads_list.append(threading.Thread(target=scan, args=(url, i)))

    # 所有线程运行
    for t in threads_list:
        t.start()


# 线程代码：扫描实现 发送get请求查看状态码
def scan(url, dic):
    r = requests.get(url)
    for line in dic:
        r = requests.get(url + line)
        if r.status_code == 200:
            print(r.url + " ： " + str(r.status_code))


muti_scan(sys.argv[1], sys.argv[2], sys.argv[3])