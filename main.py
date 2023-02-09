import wallpaper
from bs4 import BeautifulSoup
import os
from urllib import request as urlreq
from urllib.parse import urljoin
import requests

WIKIPEDIA_URL = "https://en.wikipedia.org/"

wikipedia_main_page = requests.get(WIKIPEDIA_URL)

wikipedia_main_page_doc = BeautifulSoup(wikipedia_main_page.text, "lxml")
mp_lower_div = wikipedia_main_page_doc.find("div", {"id": "mp-lower"})
original_photo_page_url = urljoin(WIKIPEDIA_URL, mp_lower_div.a.attrs["href"])
original_photo_doc = requests.get(original_photo_page_url)
original_photo_page_doc = BeautifulSoup(original_photo_doc.text, "lxml")
photo_link = ""
for i in original_photo_page_doc.findAll("a"):
    if i.text == "Original file":
        photo_link = "https:" + i.attrs["href"]
        print(i.attrs["href"])
        print(photo_link)
        break

if not os.path.exists("POTD"):
    os.mkdir("POTD")
if not os.path.exists("archive"):
    os.mkdir("archive")

os.chdir("POTD")

file_name = photo_link.split("/")[-1]
if file_name in os.listdir():
    if len(os.listdir()) > 1:
        for i in os.listdir():
            if i == file_name:
                continue
            else:
                os.replace(i, "../archive/" + i)

    print("You already got this picture")
elif not os.listdir():
    urlreq.urlretrieve(photo_link, file_name)
else:
    for i in os.listdir():
        os.replace(i, "../archive/" + i)

    urlreq.urlretrieve(photo_link, file_name)

wallpaper.set(file_name)

