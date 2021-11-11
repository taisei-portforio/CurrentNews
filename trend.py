import urllib.request
from bs4 import BeautifulSoup
import re # 正規表現操作

url = 'https://search.yahoo.co.jp/realtime' # スクレイピング先
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/81.0.4044.138 Safari/537.36 '
def gettrend(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua}) #ua偽装
    html = urllib.request.urlopen(req) #偽装したreqでurlopenする
    soup = BeautifulSoup(html, "html.parser") #beautifulSoupオブジェクトの作成

    trendsindex = soup.find('section', attrs={'class':'Trend_container__2vkJ-'}) # サイトの目的の部分を抽出
    trends = trendsindex.find_all("li") #sectionタグの中のliタグを全て取得
    trlist = [] # この中にどんどん入れていく

    for trend in trends: #それぞれのliタグごとのリンクと名前を抽出
        trlist.append(trend.find('a').contents[2].string)
        trlist.append("https://search.yahoo.co.jp" + trend.find('a').attrs['href'])    
    trlist = re.sub(r'(([^,]*,){1})', r'\1\n', str(trlist))
    return trlist

    # print(trend.find('a').contents[2].string)
    # print("https://search.yahoo.co.jp" + trend.find('a').attrs['href'])