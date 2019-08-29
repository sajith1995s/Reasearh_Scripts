from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

ram = []
vga = []
cpu = []
motherboard = []
hard_disk = []

def insertRedlineDetails(page_html):
    # HTML Parsing
    content = soup(page_html, "html.parser")

    ################### VGA ########################
    containers = content.findAll("div", {"id", "0"})

    containers = content.findAll("div", {"id", "761618297"})

    ################### Hard_Disk ########################
    containers = content.findAll("div", {"id", "7"})


url = 'https://docs.google.com/spreadsheets/d/1Ah8zS-SJijt3VQT0dKK7yVhVBLO-emiG2AKak-mrB4E/pub?gid=25#'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
insertRedlineDetails(page_html)