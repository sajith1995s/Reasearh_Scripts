from selenium import webdriver
import re
import sys
import pymongo
import time

chrome_path = "..\chromeDriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get("https://store.steampowered.com/")

# get game name by ommand-line argument
# search_tag = sys.argv[1]

#  games not age check: far cry 4 | Call of Duty®: Modern Warfare® 3 | crysis | call of duty 4 | pubg | far cry 5 | Need For Speed | gta v | Tomb Raider | anno | assassins creed origins
#  games  age check: Call of Duty 7: Black Ops | call of duty ww2
search_tag = 'Call of Duty 7: Black Ops'

# search the game
search_game = driver.find_element_by_id("store_nav_search_term")
search_game.send_keys(search_tag)
search_game.submit()

#  click first game in the search results
driver.find_element_by_xpath("""//*[@id="search_result_container"]/div[2]/a[1]""").click()

# get age check url
url = driver.current_url
print(url)

if ("agecheck" in url):
    print("Age Checked")
    # driver.find_element_by_xpath("""// *[ @ id = "ageYear"]""").click()
    search_game = driver.find_element_by_id("ageYear")
    search_game.send_keys("2000")
    driver.find_element_by_class_name("btnv6_blue_hoverfade").click()
    time.sleep(5)

else :
    print("Age Not-Checked")

# get game image
image = driver.find_element_by_class_name("game_header_image_full")
image_url = image.get_attribute("src")
print(image_url)

# game name
game_name_element = driver.find_element_by_class_name("apphub_AppName")
game_name = game_name_element.text

# Get minimum system requirements
try:
    minimum_requirements = driver.find_element_by_xpath("""//ul[contains(.,'Processor: ')]""")
    print(minimum_requirements.text)
except:
  print("Minimum Requirements Not Available")

print("------------------------------------------------------------------------------------------------------------------------------------------")

# Get recommended system requirements if exists
try:
    recommended_requirements = driver.find_element_by_xpath("""//div[@class='game_area_sys_req_rightCol' and ./ul[contains(.,'Processor: ')]]""")
    print(recommended_requirements.text)
    recomended_requirements = 0
except:
  print("Recommended Requirements Not Available")

print("----------------------------------------------------------")

# split the requirements by new line and ":"
requirement = minimum_requirements.text
data = re.split(': |\n', requirement)

# get the indexes of pc parts
for x in range(len(data)):
  # print(data[x])
  if data[x] == "Processor":
      cpu_index = x+1

  if data[x] == "Memory":
      memory_index = x+1

  if (data[x] == "Video Card" or data[x] == "Graphics"):
      graphics_index = x+1

  if (data[x] == "Hard Disk Space" or data[x] == "Storage" or data[x] == "Hard Drive" or data[x] == "Disk Space"):
      storage_index = x+1

# game name
print(game_name)
# cpu
cpu = data[cpu_index]
print(cpu)
#  memory
memory = data[memory_index]
print(memory)
# graphics
graphics = data[graphics_index]
print(graphics)
# storage
storage = data[storage_index]
print(storage)


# insert game in to mongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
database = myclient["techRingdb"]
collection = database["games"]

game = { "name": game_name,
         "cpu": cpu,
         "ram": memory,
         "graphics": graphics,
         "storage": storage,
         "imageSource": image_url
         }

x = collection.insert_one(game)