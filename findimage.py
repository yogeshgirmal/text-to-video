
import time
import requests
import urllib.request
import os
from PIL import Image
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class findimage():
	def __init__(self, head = True):

		chrome_options = Options()
		os.system('mkdir downloads')

		if not head:
			chrome_options.add_argument("--headless")  
		chromedriver_path = "chromedriver.exe"
		service = Service(executable_path=chromedriver_path)
		self.browser = webdriver.Chrome(service= service, options=chrome_options) 

	count = 1

	def getImg(self, name, count):

		done = False

		while not done:
			try:
				self.browser.get(f"https://pixabay.com/images/search/{name}/")
				time.sleep(0.1)
				images= self.browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[3]/div/div/div/a/picture/img")
				time.sleep(0.1)
				src = images.get_attribute('src')

				os.chdir('./downloads')

				response= requests.get(src, stream=True)
				with open(f"{count}.jpg",'wb') as out_file:
					shutil.copyfileobj(response.raw, out_file)
				del response	
				os.chdir('..')
				count +=1
				done = True
			except ValueError:
				print("Img not found")
				

	def close(self):
		self.browser.quit()