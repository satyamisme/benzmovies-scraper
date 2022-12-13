
import time
from bs4 import BeautifulSoup
import requests
from requests import get

url = "https://benzmovies.site/2-0-2018-telugu-full-movie-download-amzn-web-dl-1080p-720p-480p-360p-240p-avc-dd5-1-640-kbps-esub/"

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
       
       
print(benz(url))
