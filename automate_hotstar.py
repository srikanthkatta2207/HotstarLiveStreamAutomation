from selenium import webdriver  
 
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By

import time

import sys

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 60) #wait time for webdriver locate

def run():

	driver.get(sys.argv[1])

	xpath = '//button[@class="vjs-big-play-button"]'
	
	wait.until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

	list = driver.find_elements_by_xpath(xpath)
	
	list[0].click()

	time.sleep(float(sys.argv[2]))

	driver.execute_script("window.open('', 'updateCart').close()")

	def get_clear_browsing_button(driver):
	   
		return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


	def clear_cache(driver):
	    
		driver.get('chrome://settings/clearBrowserData')

		wait.until(get_clear_browsing_button)

		get_clear_browsing_button(driver).click()

	   	wait.until_not(get_clear_browsing_button)

	clear_cache(driver)


while(1):
	run()