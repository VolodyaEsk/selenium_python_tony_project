# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.implicitly_wait(15)
search_field = driver.find_element_by_css_selector("input[name=q]")
print search_field
print "Firefox successes"
driver.quit()


driver = webdriver.Chrome()
driver.get("http://www.google.com")
wait = WebDriverWait(driver, 10)
fLocator = "input[name=q]"
try:
    search_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))
    print search_field
    print "Chrome successes"
except TimeoutException:
    print "Element is not found"
finally:
    driver.quit()


