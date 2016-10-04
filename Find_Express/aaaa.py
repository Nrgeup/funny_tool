import urllib.request
import urllib.parse
import json
while True:
    kuaidinu=(input("输入单号/输入‘esc’退出查询"))
    if kuaidinu=="esc":
        break
    x=0
    dict={}
    url="http://www.kuaidi100.com/autonumber/autoComNum?text="+kuaidinu
    html=urllib.request.urlopen(url).read()
    html=html.decode('utf-8')
    html=json.loads(html)
    autonumber=html["auto"]
    if len(html["auto"])==0:
        print ("眼蒙了吧！，重新输入吧")
        continue
    autolistnumber=len(autonumber)
    while x<autolistnumber:
        x2=x
        print ()
        ac=autonumber[x2]["comCode"]
        x+=1
        dict[x]=ac
        print ((str(x)+"、")+autonumber[x2]["comCode"])

    number=int(input("\n输入对应快递商序列号"))
    url2="http://www.kuaidi100.com/query?type="+dict[number]+"&"+"postid="+kuaidinu
    html2=urllib.request.urlopen(url2).read()
    html2=html2.decode("utf-8")
    html2=json.loads(html2)
    if (html2["message"])!="ok":
        print("手残输错了吧or快递公司是个坑！")
        continue
    #print ("查询时间："+(html2["updatetime"])+"\n")
    print ("最新时间："+html2["data"][0]["time"]+"\n"+"最新位置："+html2["data"][0]["context"]+"\n")

print ('结束使用，小Q练手制作')

