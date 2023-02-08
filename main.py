import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service

import logging
logging.getLogger('WDM').setLevel(logging.NOTSET)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
service=Service(ChromeDriverManager().install())
b = webdriver.Chrome(service=service, options=options)

input_word = sys.argv[1]

def google(input_word):
	url = "https://google.com/search?q=" + input_word
	try:
		b.get(url)
		div = b.find_element(By.XPATH, "//div[@class='kno-rdesc']")
		span = div.find_element(By.TAG_NAME, "span")
		print(span.text)
		return True
	except:
		print("searching wiki...")
		return False

def wiki(input_word):
	url = "https://ja.wikipedia.org/wiki/" + input_word
	try:
		b.get(url)
		content = b.find_element(By.CLASS_NAME, "mw-parser-output")
		p = content.find_element(By.TAG_NAME, "p")
		print(p.text)
	except:
		print("could not find.")

if google(input_word) is False:
	wiki(input_word)
