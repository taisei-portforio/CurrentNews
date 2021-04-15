import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.yahoo.co.jp/realtime'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/81.0.4044.138 Safari/537.36 '
def gettrend(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")

    trendsindex = soup.find('section', attrs={'class':'Trend_container__2vkJ-'})
    trends = trendsindex.find_all("li")
    trlist = []

    for trend in trends:
        trlist.append(trend.find('a').contents[2].string)
        trlist.append("https://search.yahoo.co.jp" + trend.find('a').attrs['href'])    
    return trlist

    # print(trend.find('a').contents[2].string)
    # print("https://search.yahoo.co.jp" + trend.find('a').attrs['href'])