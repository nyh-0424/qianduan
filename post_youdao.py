import random
import  time
import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content='我和你'

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    # print("random=",s)
    # print("ts=",t)
    # print("salt=",t+s)
    return t+s
    # return '15846844357889'


def get_md5(value):
    import hashlib
    m = hashlib.md5()
    m.update(value.encode("utf-8"))
    return m.hexdigest()


def get_sign():
    i=get_salt()
    e=get_content()
    s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    # print("s=",s,"  md5=",get_md5(s))
    return get_md5(s)
    # return '4cf44da69384da8fb5c2364a31b22380'


def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    print("ts=",ts)
    return ts    #'1584684435788'

def get_content():
    return content

form_data={
    'i': get_content(),
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}



def get_headers():
    headers={
        'Cookie': 'OUTFOX_SEARCH_USER_ID = 1972308305 @ 10.169.0.83',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    return headers

class Youdao():
    def __init__(self):
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sigm=self.get_sign()





if __name__ == '__main__':
    ts=get_ts()
    print(form_data)
    print(get_headers())
    response=requests.post(url,data=form_data,headers=get_headers())
    print(response.text)