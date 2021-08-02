# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
import sys


def scan_port(port):
    ip = sys.argv[1]
    try:
        s = socket.socket(2, 1)
        res = s.connect_ex((ip, port))
        if res == 0:  # 如果端口开启 发送 hello 获取banner
            print('Port {}: OPEN'.format(port))
        s.close()
    except Exception as e:
        print(str(e.message))


def init_set(ip_adress, threads, time, type, port_s, port_e):
    remote_server_ip = ip_adress  # ip地址
    ports = []
    print('-' * 60)
    print('Please wait, scanning remote host ', remote_server_ip)
    print('-' * 60)
    socket.setdefaulttimeout(float(time)/1000.0)  # 设置超时时间
    if type == "全扫描":
        for i in range(1, 65535):
            ports.append(i)
    elif type == "常规扫描":
        ports = [20, 21, 22, 23, 25, 53, 80, 81, 102, 109, 110, 119, 135, 137, 138, 139, 161, 443, 445, 554, 1024, 1080,
                 1755, 4000, 5554, 5632, 8080]  # 常规端口
    else:
        for i in range(int(port_s), int(port_e)+1):
            ports.append(i)
    # Check what time the scan started
    t1 = datetime.now()
    pool = ThreadPool(processes=int(threads))  # 创建进程
    results = pool.map(scan_port, ports)
    pool.close()
    pool.join()
    print('Multiprocess Scanning Completed in  ', datetime.now() - t1)  # 显示运行的时间


#  传递参数，包括 ip地址，线程数、超时时间、扫描类型、扫描起始端口和终止端口
init_set(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])