import requests
from bs4 import BeautifulSoup as bs
import os

htmlDoc = requests.get("https://en.wikipedia.org/wiki/Main_Page")

soup = bs(htmlDoc.text, "lxml")
mpLowerDiv = soup.find("div", {"id": "mp-lower"})
originalPhotoPageUrl = "https://en.wikipedia.org/" + mpLowerDiv.a.attrs["href"]
originalPhotoDoc = requests.get(originalPhotoPageUrl)
soup = bs(originalPhotoDoc.text, "lxml")
photoLink = ""
for i in soup.findAll("a"):
    if i.text == "Original file":
        photoLink = "https:" + i.attrs["href"]
        print(i.attrs["href"])
        print(photoLink)
        break
photo = requests.get(photoLink)
fileFormat = photoLink.split(".")[-1]
if os.path.exists("photo"):
    os.chdir("photo")
else:
    os.mkdir("photo")
    os.chdir("photo")
# requests module couldn't get data from the link(403 error)
os.system("wget " + photoLink)
name = os.listdir()[0]
os.system("gsettings set  org.gnome.desktop.background picture-uri-dark " + "\"file://" + os.getcwd() + "/" + name + "\"")

