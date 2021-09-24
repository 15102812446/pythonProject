import requests
url = 'http://www.baidu.com/'
strhtml = requests.get(url)#git方式获取网页数据,存至strhtml变量
print(strhtml.text)#文本形式输出网页