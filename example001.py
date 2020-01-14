import requests
url="http://www.cnblogs.com/hjw1"
try:
    r=requests.get(url)
#r.raise_for_status()的功能是判断返回的状态码，如果状态码不是200（如404），则抛出异常
    r.raise_for_status()
    print (r.encoding)
    print ( r.text)
except:
    print ("failed")