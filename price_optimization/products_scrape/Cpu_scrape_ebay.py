#Import Libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
import re
import test2

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["techRingdb"]
cpu_array = []

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
            capacity = ''
            model = ''
            socket = ''
            cores = ''
            series = ''
            proccessor_type = ''
            speed = ''

            if content1.find("h1", {"id": "itemTitle"}):
                name = content1.find("h1", {"id": "itemTitle"}).get_text()
            if content1.find("div", {"id": "vi-itm-cond"}):
                condition = content1.find("div", {"id": "vi-itm-cond"}).get_text()
            if content1.find("span", {"id": "prcIsum"}):
                price = content1.find("span", {"id": "prcIsum"}).text
            else:
                price = content1.find("span", {"id": "prcIsum_bidPrice"}).text
            if content1.find("span", {"id": "vi-ret-accrd-txt"}):
                warranty = content1.find("span", {"id": "vi-ret-accrd-txt"}).get_text()
            if content1.find("img", {"id": "icImg"}):
                image = content1.find("img", {"id": "icImg"}).get("src")

            table = content1.find("div", {"class": "itemAttr"})

            tds = table.findAll("td")
            count1 = 0
            array = []
            for td in tds:
                array.append(td.text.strip())

            for array_item in array:
                if "Socket Type:" in array_item:
                    socket = array[count1 + 1]
                elif "Processor Type:" in array_item:
                    proccessor_type = array[count1 + 1]
                elif "Clock Speed:" in array_item:
                    speed = array[count1 + 1]
                count1 = count1 + 1

            mydict = {"name": name, "size": capacity, "price": price, "warranty": warranty, "image": image,
                      "owner": "ebay", "model": model, "socket": socket, "speed": speed,
                      "proccessor_type": proccessor_type}
            cpu_array.append(mydict)
            mydoc = mycol.find({"name": name})




url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=cpu&_sacat=0'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
mycol = mydb["RAM"]
insertEbayDetails(page_html)