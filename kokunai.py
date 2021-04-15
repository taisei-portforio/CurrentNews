import urllib.request
from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/81.0.4044.138 Safari/537.36 '

def getkokunai(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    
    topicsindex = soup.find('div', attrs={'class':'sc-bwCtUz frWYWL'})
    topics = topicsindex.find_all("li")
    knlist = []

    for topic in topics:
        knlist.append(topic.find('a').contents[0].string)
        knlist.append(topic.find('a').attrs['href'])
        
  
    # knlist = re.sub(r'(([^,]*,){1})', r'\1\n', str(knlist))    
    return knlist

    # print(trend.find('a').contents[2].string)
    # print("https://search.yahoo.co.jp" + trend.find('a').attrs['href'])
    