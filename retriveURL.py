from typing import overload
import requests
from bs4 import BeautifulSoup

def getURL_manu():
    page = requests.get(url = input('Please input URL: '))
    # page = requests.get('https://funestnews.com/view1/32485/')

    pageDoc = page.text

    soup = BeautifulSoup(pageDoc, 'lxml')


    videoTagString = soup.find('video', class_ = 'wp-video-shortcode')

    videoURL = videoTagString.find('a').string
    # print(videoURL)
    return videoURL

