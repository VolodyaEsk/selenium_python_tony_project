# -*- coding: utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.google.com")
print "Firefox successes"
driver.quit()


driver = webdriver.Chrome()
driver.get("http://www.google.com")
print "Chrome successes"
driver.quit()


