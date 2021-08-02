# coding: utf-8
'''　多线程 Socket TCP 端口扫描器  by: EvilCLAY'''
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

# remote_server = raw_input("Enter a remote host to scan:")
# remote_server_ip = socket.gethostbyname(remote_server)
remote_server_ip = "10.16.14.171"
ports = []

print('-' * 60)
print('Please wait, scanning remote host ', remote_server_ip)
print('-' * 60)

socket.setdefaulttimeout(0.5)


def scan_port(port):
    try:
        s = socket.socket(2, 1)
        res = s.connect_ex((remote_server_ip, port))
        if res == 0:  # 如果端口开启 发送 hello 获取banner
            print ('Port {}: OPEN'.format(port))
        s.close()
    except Exception as e:
        print(str(e.message))


for i in range(1, 1025):
    ports.append(i)

# Check what time the scan started
t1 = datetime.now()

pool = ThreadPool(processes=64)
results = pool.map(scan_port, ports)
pool.close()
pool.join()

print ('Multiprocess Scanning Completed in  ', datetime.now() - t1)