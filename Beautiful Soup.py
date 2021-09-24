import requests
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
date = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(date)