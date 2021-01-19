#为了高效处理网络 I/O，需要使用并发，因为网络有很高的延迟，所以为了不浪费 CPU 周
#期去等待，最好在收到网络响应之前做些其他的事。
import os
import time
import sys
import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = ''

def save_flag(img,filename):
    path = os.path.join(DEST_DIR,filename)
    with open(path,'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL,cc = cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text,end = ' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image,cc.lower()+'.gif')
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count,elapsed))

if __name__ == '__main__':
    main(download_many)