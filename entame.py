import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/81.0.4044.138 Safari/537.36 '

def getentame(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    
    topicsindex = soup.find_all('div', attrs={'class':'sc-jqCOkK gRKalU'})[3]
    topics = topicsindex.find_all("li")
    enlist = []

    for topic in topics:
        enlist.append(topic.find('a').contents[0].string)
        enlist.append(topic.find('a').attrs['href'])
        
    enlist = re.sub(r'(([^,]*,){1})', r'\1\n', str(enlist))    
    return enlist