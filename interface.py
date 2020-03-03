import requests
import pytest



class TestMubu:

   def test_mubu(slef):
       url="http://mubu.com/"
       method="GET"
       heraders={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
              }
       kwargs={
           "headers":heraders,
           "verify":False
       }
       res=requests.request(method,url,**kwargs)
       assert res.status_code == 200
       print(res.content)
   def test_login_sumbit(self):
       url="https://mubu.com/api/login/submit"
       method="POST"
       headers={
           "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.70Safari / 537.36",
           "content-type": "application/x-www-form-urlencoded;charset=UTF-8"
       }
       kwargs = {
           "headers": headers,
           "verify": False,
           "data" : "phone=18813037753&password=13261297907&remember=true"
       }
       res=requests.request(method,url,**kwargs)
       print(res.request)
       code=res.json()["code"]
       assert code == 0
       print(res.json())
