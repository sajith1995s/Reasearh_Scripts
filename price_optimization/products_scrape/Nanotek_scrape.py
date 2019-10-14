from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

ram = []
vga = []
cpu = []
motherboard = []
hard_disk = []


def insertNanotekDetails(page_html):
    # HTML Parsing
    content = soup(page_html, "html.parser")

    name = ''
    price = ''
    warranty = ''
    image = ''
    capacity = ''
    model = ''
    socket = ''
    proccessor_type = ''
    speed = ''
    capacity = ''
    type = ''

    containers = content.findAll("div", {"id": "sheets-viewport"})

    ################### CPU ########################

    for con in containers:
        list = con.find("div", {"id": "0"})
        table = list.find("tbody")
        trs = table.findAll("tr")
        for tr in trs:
            tds = tr.findAll("td")
            count1 = 0
            for td in tds:
                if "Socket" in td.text:
                    socket = ''
                    print(td.text)
                    header_arr = td.text.split(" ")
                    socket_count = 0
                    for a in header_arr:
                        print(header_arr[3])
                    warranty = td.text
                    break
                else:
                    if count1 == 0:
                        name = td.text
                    elif count1 == 1:
                        price = td.text
                count1 = count1 + 1
    # header = 'Socket 1151 Processors 3 Years Warranty 9th Generation'
    # header_arr = header.split(" ")
    # if header_arr[0] == "Socket":
    #     socket = header_arr[1]
    # elif header_arr[2] == "Socket":
    #     socket = header_arr[3]
    #
    # count = 0
    # for x in header_arr:
    #     if x == "Years":
    #         warranty = header_arr[count-1]+" "+x+" "+header_arr[count+1]
    #     count=count+1
    #
    # name = "Intel® Core™ i9-9900K (16M Cache, up to 5.00 GHz)"
    # arr = name.split(" (")
    # brand = arr[0].split()[0]
    # if "Intel" in brand:
    #     brand = brand.strip(brand[5])
    # speed = arr[1].strip(")")
    #
    # name = "AMD Ryzen™ 5 3600 (up to 4.2Ghz 6-cores 12-threads) 35M Cache"
    # arr = name.split(" (")
    # brand = arr[0].split()[0]
    # second_arr = arr[1].split(")")
    # speed = second_arr[0]

    # Check whether the product is already in the database
    # If so check the price for the push notification

    # Call Sorting script to get rating

    # Call Sentiment Analysis script to get user review ratings

    # Insert to database

    ################### Motherboard ########################
    # for con in containers:
    #     list = con.find("div", {"id": "2099928543"})
    #     table = list.find("tbody")
    #     trs = table.findAll("tr")
    #     for tr in trs:
    #         tds = tr.findAll("td")
    #         count1 = 0
    #         for td in tds:
    #             if "Socket" in td.text:
    #                 socket = td.text
    #                 warranty = td.text
    #                 break
    #             else:
    #                 if count1 == 0:
    #                     name = td.text
    #                 elif count1 == 1:
    #                     price = td.text
    #             count1 = count1 + 1

    # header = 'Socket 1151 Asus Motherboards 9th / 8th Generation'
    # price = 0
    # socket = ''
    # warranty = ''
    # header_arr = header.split()
    # count = 0
    # for x in header_arr:
    #     if x == "Socket":
    #         socket = header_arr[count+1]
    #     count = count+1
    #
    # name = "ROG MAXIMUS XI FORMULA wifi"
    # arr = name.split(" ")
    # if arr[0].lower() == "rog" or arr[0].lower() == "asus":
    #     model = arr[0]
    # elif arr[0].lower() == "gigabyte":
    #     model = arr[0]
    # elif arr[0] == "MSI":
    #     model = arr[0]
    #
    # print(arr[0])

    ################### RAM ########################
    # for con in containers:
    #     list = con.find("div", {"id": "2099928543"})
    #     table = list.find("tbody")
    #     trs = table.findAll("tr")
    #     for tr in trs:
    #         tds = tr.findAll("td")
    #         count1 = 0
    #         for td in tds:
    #             if "Ram" in td.text:
    #                 warranty = td.text
    #                 type = td.text
    #                 break
    #             else:
    #                 if count1 == 0:
    #                     name = td.text
    #                 elif count1 == 1:
    #                     price = td.text
    #             count1 = count1 + 1

    ################### VGA ########################
    # list = con.find("div", {"id": "274725464"})
    # table = list.find("tbody")
    # trs = table.findAll("tr")
    # for tr in trs:
    #     tds = tr.findAll("td")
    #     count1 = 0
    #     for td in tds:
    #         if "warranty" in td.text.lower():
    #             warranty = td.text
    #             break
    #         else:
    #             if count1 == 0:
    #                 name = td.text
    #             elif count1 == 1:
    #                 price = td.text
    #         count1 = count1 + 1

    ################### Hard_Disk ########################
    # list = con.find("div", {"id": "1754104783"})
    # table = list.find("tbody")
    # trs = table.findAll("tr")
    # for tr in trs:
    #     tds = tr.findAll("td")
    #     count1 = 0
    #     for td in tds:
    #         if "warranty" in td.text.lower():
    #             warranty = td.text
    #             break
    #         else:
    #             if count1 == 0:
    #                 name = td.text
    #             elif count1 == 1:
    #                 price = td.text
    #         count1 = count1 + 1


url = 'https://docs.google.com/spreadsheets/d/1ZMGJc69uk2fVEFPKNu1UboxE3Wh5ftI9yUJuIbQzZi4/pubhtml?fbclid=IwAR1IvrZ6t9p55FoU_p93990rMbza2DSs6L_2WlrD64xAMTywyh8MZ3ncwD0#'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
insertNanotekDetails(page_html)
