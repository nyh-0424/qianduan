import  requests

url="http://www.cntour.cn"

response=requests.get(url)
print(response.text)