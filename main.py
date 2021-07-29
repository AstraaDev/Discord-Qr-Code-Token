from selenium import webdriver
import time
import urllib.request
from PIL import Image

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
driver.get('https://discord.com/login')
time.sleep(10)
qrcode = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/form/div/div/div[3]/div/div/div/div[1]/div[1]/img")
link = qrcode.get_attribute("src")
urllib.request.urlretrieve(link, "img/qrcode.png")
bg = Image.open('img/back.png')
qrcode = Image.open('img/qrcode.png')
qrcode = qrcode.resize(size=(127, 127))
bg.paste(qrcode, (87, 313))
discord = Image.open('img/discord.png')
discord = discord.resize(size=(40, 40))
bg.paste(discord, (130, 355), discord)
bg.save('gift/nitroGift.png')