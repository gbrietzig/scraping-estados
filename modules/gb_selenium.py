from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

def config_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--headless") 
    return chrome_options

def create_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=config_chrome_options())
    driver.implicitly_wait(0.00001)
    return driver

def access_url(url, driver):
    driver.get(url)

def insert_text(element, text):
    while True:
        try:
            element.clear()
            element.send_keys(text)
            if element.get_attribute('value') == text:
                break
        except:
            time.sleep(5)

def btn_click(element):#, force, driver):
    while True:
        try:
            # script=element.get_attribute('onclick')
            # if script==None or force:
                element.click()
            # else:
            #     driver.execute_script(script)
                break
        except:
            time.sleep(5)

def catch_element(attribute, value, container):
    while True:
        try:
            if attribute==3:
                return Alert(container)
            elif attribute==0:
                return container.find_element(By.XPATH, value)
            elif attribute==1:
                return container.find_element(By.TAG_NAME, value)
        except:
            time.sleep(5)

def catch_elements(attribute, value, container):
    while True:
        try:            
            if attribute==0:
                return container.find_elements(By.XPATH, value)
            elif attribute==1:
                return container.find_elements(By.TAG_NAME, value)
        except:
            time.sleep(5)