#Import Libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
import re

motherboard = []

def insertEbayDetails(page_html):
    # HTML Parsing
    content = soup(page_html, "html.parser")

    list = content.findAll("div", {"id": "srp-river-results"})
    count = 0
    link_more = ''

    containers = content.findAll("li", {"class": "s-item"})
    for container in containers:
        if count != 0:
            link_more = container.find("a", {"class", "s-item__link"})["href"]
            uClient1 = uReq(link_more)
            page_html1 = uClient1.read()
            uClient1.close()

            content1 = soup(page_html1, "html.parser")

            name = ''
            price = ''
            warranty = ''
            image = ''
            condition = ''
            model = ''
            capacity = ''
            type = ''
            speed = ''

            if content1.find("h1", {"id": "itemTitle"}):
                name = content1.find("h1", {"id": "itemTitle"}).get_text()
            if content1.find("div", {"id": "vi-itm-cond"}):
                condition = content1.find("div", {"id": "vi-itm-cond"}).get_text()
            if content1.find("span", {"id": "prcIsum"}):
                price = content1.find("span", {"id": "prcIsum"}).text
            else:
                price = content1.find("span", {"id": "mm-saleDscPrc"}).text
            if content1.find("span", {"id": "vi-ret-accrd-txt"}):
                warranty = content1.find("span", {"id": "vi-ret-accrd-txt"}).get_text()
            if content1.find("img", {"id": "icImg"}):
                image = content1.find("img", {"id": "icImg"}).get("src")

            table = content1.find("div", {"class": "itemAttr"})
            if table.find("h2", {"itemprop": "model"}):
                model = table.find("h2", {"itemprop": "model"}).text
            if table.find("h2", {"itemprop": "model"}):
                model = table.find("h2", {"itemprop": "model"}).text

            tds = table.findAll("td")
            count1 = 0
            array = []
            for td in tds:
                array.append(td.text.strip())

            for array_item in array:
                if "Total Capacity:" in array_item:
                    capacity = array[count1 + 1]
                elif "Type:" in array_item:
                    type = array[count1 + 1]
                elif "Bus Speed:" in array_item:
                    speed = array[count1 + 1]
                count1 = count1 + 1

            mydict = {"name": name, "size": capacity, "price": price, "type": type,
                      "warranty": warranty, "image": image, "owner": "ebay", "model": model}
            motherboard.append(mydict)

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=motherboard&_sacat=0'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
insertEbayDetails(page_html)