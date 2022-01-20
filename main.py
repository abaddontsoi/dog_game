import requests
import retriveURL

import urllib.request

try:
    url = retriveURL.getURL_manu()

    print(url)

    video = requests.get(url)

    print(video.status_code)

    name = input('Enter file name: ') + '.mp4'
    urllib.request.urlretrieve(url, name)

except Exception as e:
    print(e)