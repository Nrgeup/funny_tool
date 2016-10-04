#!/usr/bin/python
# encoding:utf-8

import json, urllib, urllib.request, hashlib, base64, urllib.parse


def encrypt(origin_data, appkey):
    "数据内容签名：把(请求内容(未编码)+AppKey)进行MD5加密，然后Base64编码"
    m = hashlib.md5()
    m.update((origin_data+appkey).encode("utf8"))

    encodestr = m.hexdigest()
    base64_text = base64.b64encode(encodestr.encode(encoding='utf-8'))
    return base64_text


def sendpost(url, datas):
    "发送post请求"
    postdata = urllib.parse.urlencode(datas).encode('utf-8')
    header = {
        "Accept": "application/x-www-form-urlencoded;charset=utf-8",
        "Accept-Encoding": "utf-8"
    }
    req = urllib.request.Request(url, postdata, header)
    get_data = (urllib.request.urlopen(req).read().decode('utf-8'))
    return get_data


def getcompany(logisticcode, appid, appkey, url):
    "获取对应快递单号的快递公司代码和名称"
    data1 = {'LogisticCode': logisticcode}
    d1 = json.dumps(data1, sort_keys=True)
    requestdata = encrypt(d1, appkey)
    post_data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '2002', 'DataType': '2',
            'DataSign': requestdata.decode()}
    json_data = sendpost(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data

def main():
    expresscode = input("请输入快递单号：")
    data = getcompany(expresscode, "1266271", "7526a46e-3a2a-4f5b-8659-d72f361e3386",
               'http://testapi.kdniao.cc:8081/Ebusiness/EbusinessOrderHandle.aspx')
    if any(data['Shippers']):
        print(data['Shippers'][0]['ShipperCode'])
        print(data['Shippers'][0]['ShipperName'])
    else :
        print("未查到该快递信息！")
    return

