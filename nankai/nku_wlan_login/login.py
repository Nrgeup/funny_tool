import urllib
import http.cookiejar
import re
import socket

url = "http://202.113.18.106:801/eportal/?c=ACSetting&a=Login&wlanuserip=" \
      "&wlanacip=null&wlanacname=null&port=&iTermType=1&mac=000000000000&ip="


def remember_cookies(req):
    """自动记住cookie"""
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    return r.read().decode('GBK')


def login(username, password):
    """模拟登录"""
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "utf-8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Host": "202.113.18.106:801",
        "Referer": "http://202.113.18.106/a70.htm",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
    }
    postdata = urllib.parse.urlencode({
        "DDDDD": username,
        "upass": password,
        "login_nei": "1",
    }).encode('utf-8')
    req = urllib.request.Request(url, postdata, header)
    respose = urllib.request.urlopen(req).read().decode('GBK')
    # respose = remember_cookies(req)
    return respose


def debug(respose):
    """Debug function!"""
    f = open('ans.txt', 'w+')
    f.write(respose)
    f.close()
    print(respose)
    return


def if_can_use(username, password):
    """测试帐号密码是否可用"""
    text = login(username, password)
    state = re.search(r"<title>登录成功</title>", text)
    if state:
        return True
    else:
        return False


def main():
    username = input("请输入上网帐号：")
    password = input("输入密码：")
    state = if_can_use(username, password)
    if state:
        print("登录成功！")
    else:
        print("登录失败！")
    return

if __name__ == '__main__':
    main()

