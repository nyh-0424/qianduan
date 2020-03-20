import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data={
    'i':'我和你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846844357889',
    'sign': '4cf44da69384da8fb5c2364a31b22380',
    'ts': '1584684435788',
    'bv': '70244e0061db49a9ee62d341c5fed82a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)