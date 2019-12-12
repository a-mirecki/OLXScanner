from importlib import reload
from lxml import html
from bs4 import BeautifulSoup
import sys
import time
import os
import urllib.request

def generateRender():
    url = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/?search%5Bfilter_float_price%3Ato%5D=850&search%5Bfilter_enum_roomsize%5D%5B0%5D=one'
    #url = 'https://www.olx.pl/oddam-za-darmo/'
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    fp = urllib.request.urlopen(req)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    #print(mystr)
    return mystr

for i in range(1):
    r = generateRender()
    soup = BeautifulSoup(str(r), 'html.parser')
    linki = soup.findAll("a",  {"class" : "marginright5 link linkWithHash detailsLink"})
    allLinks = []
    linksToSend = []

    if len(linki) < 1:
        print("Nie znaleziono mieszkan - HTTP Error")

    for i in linki:
        allLinks.append(i['href'])


    with open ("linki.txt", "r") as my_file:
        content = my_file.readlines()
    content = [x.strip() for x in content]

    for i in allLinks:
        if i not in content:
            linksToSend.append(i)

    if len(linksToSend) > 0:
        for x in linksToSend:
            print(x+"\n")
        os.system("mpg321 gadu.mp3")

    with open("linki.txt", "w") as my_file:
        for i in allLinks:
            my_file.write(i+"\n")
