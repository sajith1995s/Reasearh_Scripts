from selenium import webdriver

chrome_path = "..\chromeDriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

# Games
# driver.get("https://store.steampowered.com/app/17330/Crysis_Warhead/")
# driver.get("https://store.steampowered.com/agecheck/app/311210/")
driver.get("https://store.steampowered.com/app/582160/Assassins_Creed_Origins/")
# driver.get("https://store.steampowered.com/app/812140/Assassins_Creed_Odyssey/")
# driver.get("https://store.steampowered.com/app/242050/Assassins_Creed_IV_Black_Flag/")
# driver.get("https://store.steampowered.com/app/47870/Need_For_Speed_Hot_Pursuit/")
# driver.get("https://store.steampowered.com/app/552520/Far_Cry_5/")
# driver.get("https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/")

# # Get minimum system requirements
# minimum_requirements = driver.find_element_by_xpath("""//ul[contains(.,'Processor: ')]""")
# print(minimum_requirements.text)
#
# print("------------------------------------------------------------------------------------------------------------------------------------------")
#
# # Get recommended system requirements if exists
# try:
#     recommended_requirements = driver.find_element_by_xpath("""//div[@class='game_area_sys_req_rightCol' and ./ul[contains(.,'Processor: ')]]""")
#     print(recommended_requirements.text)
#     recomended_requirements = 0
# except:
#   print("Recommended Requirements Not Available")

url = driver.current_url
print(url)

if ("agecheck" in url):
    print("qqqqqqqqqqq")



import requests

game1 = {
		"name": "12344",
		"cpu": "Intel Core 2 Duo E4600 2.4GHz / AMD Athlon 64 X2 Dual Core 4200+",
		"ram": "2 GB ",
		"graphics": " NVIDIA GeForce 7800 GT 2 GB",
		"storage": " 8 GB ",
		"imageSource":"https://i.ytimg.com/vi/aWfuFZ0VJZY/maxresdefault.jpg"
	}

# insert game by backend
responce = requests.post("http://localhost:8080/api-techRing/games/create", json=game1)

print(responce.status_code)
print(responce.json())


# run python script from java
# public void runPython()
# { //need to call myscript.py and also pass arg1 as its arguments.
#   //and also myscript.py path is in C:\Demo\myscript.py
#
#     String[] cmd = {
#       "python",
#       "C:/Demo/myscript.py",
#       this.arg1,
#     };
#     Runtime.getRuntime().exec(cmd);
# }