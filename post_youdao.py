import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846844357889'


def get_sign():
    return '4cf44da69384da8fb5c2364a31b22380'


def get_ts():
    import  time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts    #'1584684435788'
          # '1585615400595'


form_data={
    'i':'我和你',
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
response=requests.post(url,form_data)
print(response.text)