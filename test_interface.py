import requests


def test_mubu():
    url="http://mubu.com/"
    heraders={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
              }
    res=requests.get(url,headers=heraders)

    print(res.content)
