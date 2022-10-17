import sys, os, time
from atexit import register
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# RMP professors list for RPI
url = 'https://www.ratemyprofessors.com/search/teachers?query=*&sid=795' 

op = Options()

#removes notifcations popup
prefs = {"profile.default_content_setting_values.notifications" : 2, 
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False}
op.add_experimental_option("prefs",prefs)

#sets up chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
driver.get(url)
driver.maximize_window()
