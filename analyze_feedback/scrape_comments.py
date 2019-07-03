from selenium import webdriver
import re
import sys
import pymongo
import time

chrome_path = "..\chromeDriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

# # hide browser
# driver.set_window_position(-10000,0)

# get site
driver.get("https://pcpartpicker.com/products/")

driver.find_element_by_xpath("""//*[@id="product-page"]/div[2]/section/div[1]/ul/li[1]/a""").click()


# get game name by ommand-line argument
# search_tag = sys.argv[1]

# serch tag of the product
#           kingston 8gb ram | intel core i7
search_tag = 'intel core i7'

# search the product
search_product = driver.find_element_by_xpath("""//*[@id="gh-ac"]""")
search_product.send_keys(search_tag)
search_product.submit()

#  click first product in the search results
driver.find_element_by_xpath("""//*[@id="navigation"]/section[2]/div/ul/li[4]/a/span/svg""").click()