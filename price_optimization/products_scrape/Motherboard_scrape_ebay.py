#Import Libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
import main_user_rating as user_rate
import Points_script as points_script
import Push_notification
import requests

motherboard = []

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["techRingdb"]

api = '4ae5b8fc2f9c52efb3b17a71c19408ac'
params = {'access_key': api, 'currencies': 'LKR,EUR,AUD,GBP', 'format': 1}

r = requests.get('http://apilayer.net/api/live', params=params)
livequote = r.json()

lkr = livequote["quotes"]["USDLKR"]
eur = ((1 / livequote["quotes"]["USDEUR"]) * lkr)
aud = ((1 / livequote["quotes"]["USDAUD"]) * lkr)
gbp = ((1 / livequote["quotes"]["USDGBP"]) * lkr)

def convert_price(p):
    cat = ""
    if "us" in p.lower():
        cat = "usd"
    elif "C" in p.lower():
        cat = "usd"
    elif "au" in p.lower():
        cat = "aud"
    elif "eur" in p.lower():
        cat = "eur"
    elif "gbp" in p.lower():
        cat = "gbp"
    try:
        p = p.replace(" ", '')
        p = p.lower().replace("usd", '').replace("us", '').replace("C", '').replace("aud", '').replace("au", '').replace("eur", '').replace("eu", '').replace("gbp", '').replace("$", '')
        if cat == "usd":
            return (float(p) * lkr).__round__(2)
        elif cat == "eur":
            return (float(p) * eur).__round__(2)
        elif cat == "aud":
            return (float(p) * aud).__round__(2)
        elif cat == "gbp":
            return (float(p) * gbp).__round__(2)
        else:
            return (float(p)).__round__(2)

    except:
        print("error in converting price")

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
            memory_type = ''
            speed = ''
            cpu_brand = ''
            pci_slot = ''
            socket = ''

            if content1.find("h1", {"id": "itemTitle"}):
                a = content1.find("h1", {"id": "itemTitle"}).get_text()
                name = a.replace('Details about   ', '')
            if content1.find("div", {"id": "vi-itm-cond"}):
                condition = content1.find("div", {"id": "vi-itm-cond"}).get_text()
            if content1.find("span", {"id": "prcIsum"}):
                price = convert_price(content1.find("span", {"id": "prcIsum"}).text)
            elif content1.find("span", {"id": "prcIsum_bidPrice"}):
                price = convert_price(content1.find("span", {"id": "prcIsum_bidPrice"}).text)
            elif content1.find("span", {"id": "mm-saleDscPrc"}):
                price = convert_price(content1.find("span", {"id": "mm-saleDscPrc"}).text)
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
                if "Total Capacity" in array_item:
                    capacity = array[count1 + 1]
                elif "Brand:" in array_item:
                    type = array[count1 + 1]
                elif "Bus Speed" in array_item:
                    speed = array[count1 + 1]
                elif "CPU Brand" in array_item:
                    cpu_brand = array[count1 + 1]
                elif "Memory Type" in array_item:
                    memory_type = array[count1 + 1]
                elif "Socket Type" in array_item:
                    socket = array[count1 + 1]
                elif "Expansion Slots" in array_item:
                    pci_slot = array[count1 + 1]
                count1 = count1 + 1

            # Call Sentiment Analysis script to get user review ratings
            user_rating = user_rate.user_rating()

            mydict = {"name": name, "size": capacity, "price": price, "type": type, "memory_type": memory_type, "cpu_brand": cpu_brand, "pci_slot": pci_slot,
                      "warranty": warranty, "image": image, "owner": "ebay", "model": model, "socket": socket, "user_rating": user_rating, "link": link_more}

            # Call Sorting script to get rating
            ratings = points_script.sorting_algorithm("motherboard", mydict)
            mydict["ratings"] = ratings
            x = mycol.insert_one(mydict)

            # # Check whether the product is already in the database
            # mydoc = mycol.find_one({"$and": [{"name": name}, {"type": type}, {"model": model}]})
            # # If so update the new price
            # if mydoc != None or mydoc != "":
            #     if mydoc["price"] != price:
            #         myquery = {"_id": mydoc['_id']}
            #         newvalues = {"$set": {"price": price}}
            #         mycol.update_one(myquery, newvalues)
            #     # check the price for the push notification
            #     if mydoc["price"] > price:
            #         Push_notification.push_notification(mydoc['_id'], mydoc['link'])
            # else:
            #     # Insert to database
            #     x = mycol.insert_one(mydict)

        count = count + 1

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=motherboard&_sacat=0'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
mycol = mydb["Motherboard"]
insertEbayDetails(page_html)