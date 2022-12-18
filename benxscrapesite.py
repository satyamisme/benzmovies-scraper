import sys
import time
from bs4 import BeautifulSoup
import requests

def benz(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    links = soup.select('a[href*="filepress"]')
    gd_txt = f"Total Links Found : {len(links)}\n\n"
    print(gd_txt) 
    for a in links:
       link = a["href"]
       print(link)

# url = "https://www.animeremux.xyz/2022/07/my-dress-up-darling-2022-anime-series.html?m=1"
site = "https://benzmovies.site/?s=telugu&post_type%5B%5D=post&post_type%5B%5D=tv"
client = requests.session()
r = client.get(site).text
soup = BeautifulSoup(r, "html.parser")
for a in soup.find_all("a"):
    c = a.get("href")
    if "720p" in c:
        x = c.split("url=")[-1]
        t = client.get(x).text
        soupt = BeautifulSoup(t, "html.parser")
        title = soupt.title
        trans = f"{(title.text)}"
        samsamlist[]
        samsamlist.append(len(samlist)) = trans
        #print(trans)
        url = x
        trans = benz(url)
        samlist.append(len(samlist)) = trans
        #print(samlist)
        result = [i for n, i in enumerate(samlist) if i not in samlist[:n]]
        a = set(samlist)
        #print(str(result))
        #print(samlist)
        seen = set(a)
        result = []
        for item in a:
            if item not in seen:
                seen.add(item)
                result.append(item)
        print(result)
