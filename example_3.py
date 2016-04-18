# coding=utf-8

import cookielib
import urllib
import urllib2
import re


class PostGetFunction:

    def __init__(self):
        self.header = {
            'Host': 'book.douban.com',
            'Content-Type': "text/html; charset=utf-8",
            'referer': 'https://www.baidu.com/link?url=reO62JpvQGJVNT2B9bEZ0Osxjo0WmrBOkGo-1_ctDn-AmjeeIuzrA5o6WsxNLdvT&wd=&eqid=b2d3e3e40000d40800000002570f0892',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
        }
        self.cookie = cookielib.LWPCookieJar()
        self.cookie_support = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.cookie_support,
                                           urllib2.HTTPHandler)
        urllib2.install_opener(self.opener)

    def post(self):
        postdata = {
        }
        postdata = urllib.urlencode(postdata)
        request = urllib2.Request(url, postdata, self.header)
        try:
            content = urllib2.urlopen(request)
            return content
        except Exception, e:
            print ("post:" + str(e))
            return None

    def get(self, url):
        request = urllib2.Request(url, None, self.header)
        try:
            content = urllib2.urlopen(request)
            str_html = content.read()
            return str_html
        except Exception, e:
            print ("open:" + str(e))
            return None

    def find_list_url(self, string):
        p1 = re.compile(r'<p class="pl">(.*)</p>')
        r1 = p1.findall(string)
        p1 = re.compile(r'title="(.*)"')
        r2 = p1.findall(string)
        p1 = re.compile(r'href="(.*)" onclick=&#34')
        r3 = p1.findall(string)
        p1 = re.compile(r'class="rating_nums">(.*)</span>')
        r4 = p1.findall(string)
        length = len(r1)

        with open('./outputs/example_3.txt', 'a') as f:
            for i in range(length):
                if r2[i] == '可试读':
                    del r2[i]
                if float(r4[i]) >= 8.5:
                    f.write(r2[i] + '\r' + r3[i] + '\r' + r1[i] + '\r\r')

if __name__ == '__main__':
    url = "https://book.douban.com/top250?start=%u"
    pgf = PostGetFunction()
    for i in range(11):
        string = pgf.get(url % (i * 25))
        pgf.find_list_url(string)

