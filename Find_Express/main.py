#!/usr/bin/python
# encoding:utf-8

import json, urllib, urllib.request, hashlib, base64, urllib.parse

#此处为快递鸟官网申请的帐号和密码
APP_id = "1266271"
APP_key = "7526a46e-3a2a-4f5b-8659-d72f361e3386"

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


def getcompany(logistic_code, appid, appkey, url):
    "获取对应快递单号的快递公司代码和名称"
    data1 = {'LogisticCode': logistic_code}
    d1 = json.dumps(data1, sort_keys=True)
    requestdata = encrypt(d1, appkey)
    post_data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '2002', 'DataType': '2',
            'DataSign': requestdata.decode()}
    json_data = sendpost(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data


def get_traces(logistic_code, shipper_code, appid, appkey, url):
    "查询接口支持按照运单号查询(单个查询)"
    data1 = {'LogisticCode': logistic_code, 'ShipperCode': shipper_code}
    d1 = json.dumps(data1, sort_keys=True)
    requestdata = encrypt(d1, appkey)
    post_data = {'RequestData': d1, 'EBusinessID': appid, 'RequestType': '1002', 'DataType': '2',
                 'DataSign': requestdata.decode()}
    json_data = sendpost(url, post_data)
    sort_data = json.loads(json_data)
    return sort_data


def recognise(expresscode):
    ""
    url = 'http://testapi.kdniao.cc:8081/Ebusiness/EbusinessOrderHandle.aspx'
    data = getcompany(expresscode, APP_id, APP_key, url)
    if not any(data['Shippers']):
        print("未查到该快递信息,请检查快递单号是否有误！")
    else :
        print("已查到该", str(data['Shippers'][0]['ShipperName'])+"("+str(data['Shippers'][0]['ShipperCode'])+")",
              expresscode)
        trace_data = get_traces(expresscode, data['Shippers'][0]['ShipperCode'], APP_id, APP_key, url)
        if trace_data['Success'] == "false" or not any(trace_data['Traces']):
            print("未查询到该快递物流轨迹！")
        else:
            str_state = "问题件"
            if trace_data['State'] == '2':
                str_state = "在途中"
            if trace_data['State'] == '3':
                str_state = "已签收"
            print("目前状态： "+str_state)
            trace_data = trace_data['Traces']
            id = 1
            for item in trace_data:
                print(str(id)+":", item['AcceptTime'], item['AcceptStation'])
                id = id + 1
            print("\n")
    return

while True:
    code = input("请输入快递单号(输入esc退出)：")
    if code == "esc":
        break
    recognise(code)
