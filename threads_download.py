import time
import urllib.request

# Bad. Wasting time waiting for network IO.
# def get_responses():
#     urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.alibaba.com', 'http://www.reddit.com']
#     start = time.time()
#     for url in urls:
#         print(url)
#         req = urllib.request.Request(
#             url,
#             data=None,
#             headers={
#                 'User-Agent': 'Python Learning Program',
#                 'From': 'hklee310@gmail.com'
#             }
#         )
#         resp = urllib.request.urlopen(req)
#         print(resp.getcode())
#     print("Elapsed time: %s" % (time.time()-start))
#
# get_responses()

from threading import Thread


class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        req = urllib.request.Request(
            self.url,
            data=None,
            headers={
                'User-Agent': 'Python Learning Program',
                'From': 'hklee310@gmail.com'
            }
        )

        resp = urllib.request.urlopen(req)
        print(self.url, resp.getcode())

def get_responses():
    urls = ['http://www.google.com', 'http://www.ebay.com', 'http://www.amazon.com', 'http://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Elapsed time: %s" % (time.time()-start))

get_responses()