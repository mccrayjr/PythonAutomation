#! /usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#see selenium docs for options like: 'start-maximized' probably adjust to stay open here?
driver.get("https://automatetheboringstuff.com")
elem = driver.find_element_by_css_selector("thing")# From this point on example code is for reference only
#you can also use .find_elements by id/class name and a host of other methods
elem.click()
elem[9].click

textInputField = driver.find_element_by_css_selector("text input")
textInputField.send_keys("string you want to type")
textInputField.submit() #automagically finds the submit corresponding to the form field

#other methods
driver.back()
driver.forward()
driver.refresh()
driver.quit()
