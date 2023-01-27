from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import requests


WIKIPEDIA_URL = "https://en.wikipedia.org/"
WIKIPEDIA_MAIN_PAGE_URL = "wiki/Main_Page"

response = requests.get(urljoin(WIKIPEDIA_URL, WIKIPEDIA_MAIN_PAGE_URL))

soup = BeautifulSoup(response.text, "lxml")
mp_lower_div = soup.find("div", {"id": "mp-lower"})
original_photo_page_url = "https://en.wikipedia.org/" + mp_lower_div.a.attrs["href"]
original_photo_doc = requests.get(original_photo_page_url)
soup = BeautifulSoup(original_photo_doc.text, "lxml")
photo_link = ""
for i in soup.findAll("a"):
    if i.text == "Original file":
        photo_link = "https:" + i.attrs["href"]
        print(i.attrs["href"])
        print(photo_link)
        break
photo = requests.get(photo_link)
file_format = photo_link.split(".")[-1]
if os.path.exists("photo"):
    os.chdir("photo")
else:
    os.mkdir("photo")
    os.chdir("photo")
# requests module couldn't get data from the link(403 error)
os.system("wget " + photo_link)
name = os.listdir()[0]
os.system("gsettings set  org.gnome.desktop.background picture-uri-dark " + "\"file://" + os.getcwd() + "/" + name + "\"")
