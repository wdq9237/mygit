import requests
url="http://www.cnblogs.com/hjw1"
try:
    r=requests.get(url)
#r.raise_for_status()�Ĺ������жϷ��ص�״̬�룬���״̬�벻��200����404�������׳��쳣
    r.raise_for_status()
    print (r.encoding)
    print ( r.text)
except:
    print ("failed")