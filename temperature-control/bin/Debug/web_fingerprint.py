import json#字典为json文件格式
import threading
import requests
import hashlib#用于md5加密
from concurrent.futures import ThreadPoolExecutor, as_completed, FIRST_EXCEPTION, wait, ALL_COMPLETED
from optparse import OptionParser

#查找cms静态文件，并计算哈希值，获取静态文件的url相对路径，根据此生成cms特征集


threadingLock = threading.Lock()
show_count = 0
SCAN_COMPLATED = False
def md5encode(text):#将关键字md5加密
    m = hashlib.md5()
    m.update(text.encode("utf-8"))
    return m.hexdigest()
def check_file_is_ok(url, path):
    """
    head 请求方式去判断文件是否存在, 减少正文响应时间
    :param url:
    :param path:
    :return:
    """
    target = url + path#拼接url和路径
    r = requests.head(target)

    if r.status_code == 200:#判断页面状态码
        return True
    return False
def get_request_md5(url, path, pattern):
    """
    通过请求路径获取内容的md5
    :param url:
    :param path:
    :param pattern:
    :return:
    """
    # print('*****************************')
    target = url + path
    r = requests.get(target)
    r_md5 = md5encode(r.text)
    print('计算得到：'+ r_md5)

    if pattern == r_md5:
        return True
    return False
def load_cms_fingers(fingers):
    """
    加载CMS指纹
    :return:
    """
    with open(fingers, encoding='gb18030',errors='ignore') as f:
        data = json.load(f)
    # print(data)
    # print("Update Time: {}".format(data.get("update_time")))
    print("CMS Fingers Count: {}".format(len(data['RECORDS'])))
    return data['RECORDS']
def read_url_file_to_list(filename):
    """
    读 URL 文件为列表
    :param filename:
    :return:
    """
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]
def check_thread(item):
    global show_count#在函数中调用全局变量
    global SCAN_COMPLATED
    url, finger = item
    path = finger.get("staticurl")
    path2 = finger.get("homeurl")
    path = path + path2 if path[0] == "/" else "/" + path

    threadingLock.acquire()
    show_count += 1
    if not SCAN_COMPLATED:
        print('\r', "扫描进度 {}/{}".format(show_count, fingers_count), end='', flush=True)
    threadingLock.release()

    if check_file_is_ok(url, path):
        print("文件存在")
        match_pattern = finger.get("checksum")
        print(match_pattern)
        result = get_request_md5(url, path, match_pattern)
        print(result)
        if result:
            threadingLock.acquire()
            if not SCAN_COMPLATED:
                print('得到目标')
                print("\nHint CMS名称: {}".format(finger.get("cmsname")))
                print("Hint 指纹文件: {}".format(finger.get("staticurl")))
                print("Hint Md5: {}\n".format(finger.get("checksum")))
                SCAN_COMPLATED = True
                threadingLock.release()
                raise Exception("任务结束")
            threadingLock.release()
if __name__ == '__main__':
    usage = "%prog -u \"http://xxxx.com\" -t threads_number"
    parser = OptionParser(usage=usage)
    print("指纹识别------2.0")
    parser.add_option("-u", "--url", dest="url", help="目标URL")
    parser.add_option("-f", "--file", dest="file", help="url文件", default=None)
    parser.add_option("-s", "--fingers", dest="fingers", help="指定指纹文件", default="cmsprint.json")
    parser.add_option("-t", "--threads", dest="threads", type="int", default=10, help="线程大小, 默认为 10")
    options, args = parser.parse_args()

    if not options.url and not options.file:
        parser.print_help()
        exit(0)

    fingers = load_cms_fingers(options.fingers)

    if options.file:
        urls = read_url_file_to_list(options.file)
    else:
        urls = [options.url]

    for url in urls:
        SCAN_COMPLATED = False
        show_count = 0

        print(" 扫描目标: {}".format(url))
        fingers_count = len(fingers)

        executor = ThreadPoolExecutor(max_workers=options.threads)
        tasks = [executor.submit(check_thread, ((url, finger))) for finger in fingers]

        wait(tasks, return_when=FIRST_EXCEPTION)

        for task in reversed(tasks):
            task.cancel()

        wait(tasks, return_when=ALL_COMPLETED)