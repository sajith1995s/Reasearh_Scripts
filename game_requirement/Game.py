from selenium import webdriver

chrome_path = "..\chromeDriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
# driver.get("https://store.steampowered.com/app/17330/Crysis_Warhead/")
# driver.get("https://store.steampowered.com/app/17300/Crysis/")
# driver.get("https://store.steampowered.com/app/582160/Assassins_Creed_Origins/")
# driver.get("https://store.steampowered.com/app/812140/Assassins_Creed_Odyssey/")
driver.get("https://store.steampowered.com/app/242050/Assassins_Creed_IV_Black_Flag/")
# driver.get("https://store.steampowered.com/app/47870/Need_For_Speed_Hot_Pursuit/")

# driver.find_element_by_xpath("""//*[@id="pb_48362"]/td[2]/a""").click()

processor = driver.find_element_by_xpath("""//ul[contains(.,'Processor:')]""")
# processor = driver.find_element_by_xpath("""/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[5]/div[2]/div[4]/div[1]/div/div/div[1]/ul/ul/li[2]""")

# memory = driver.find_element_by_xpath("""/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[5]/div[2]/div[5]/div[1]/div/div/div[1]/ul/ul/li[3]""")
# graphics = driver.find_element_by_xpath("""/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[5]/div[2]/div[5]/div[1]/div/div/div[1]/ul/ul/li[4]""")
# storage = driver.find_element_by_xpath("""/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[5]/div[2]/div[5]/div[1]/div/div/div[1]/ul/ul/li[8]""")


print(processor.text)
# print(memory.text)
# print(graphics.text)
# print(storage.text)


# //ul[@class='bb_ul' and ./li[contains(.,'Processor: ')]]
# //div[@class='game_area_sys_req_rightCol' and ./ul[contains(.,'Processor: ')]]
# //ul[contains(.,'Processor: ')]