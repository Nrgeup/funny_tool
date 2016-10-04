#!/usr/bin/python
# encoding:utf-8

import json, urllib, urllib.request, hashlib, base64, urllib.parse, http.client

#appid = "1266271"    9610107484156
#appkey = "7526a46e-3a2a-4f5b-8659-d72f361e3386"


def encrypt(data, appkey):
    "数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"
    m = hashlib.md5()
    m.update((data+appkey).encode("utf8"))
    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
    return base64_text


def sendpost(url, datas):
    "发送post请求"
    print("发送post请求")
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(url, 80)
    conn.request('POST', '/ippinte/api/scene/getall', datas, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read().decode('utf-8')
    print(data)
    conn.close()
    print("结束post请求")
    return


def getorder(LogisticCode, appid, appkey, url):
    "aaa"
    data1 = {'LogisticCode': LogisticCode}
    d1 = json.dumps(data1, sort_keys=True)
    print(d1)
    requestdata = encrypt(d1, appkey)

    data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '2002', 'DataType': '2', 'DataSign': requestdata.decode()}
    print(data)

    #sendpost(url, d2)
    return



print(encrypt("xsxsxsx","azaza"))
print(base64.b64decode(encrypt("xsxsxsx","azaza")))
getorder("9610107484156", "1266271", "7526a46e-3a2a-4f5b-8659-d72f361e3386", 'http://testapi.kdniao.cc:8081/Ebusiness/EbusinessOrderHandle.aspx')




