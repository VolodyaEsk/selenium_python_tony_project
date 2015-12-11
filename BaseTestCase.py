# -*- coding: utf-8 -*-

from selenium import webdriver
from constants import TT_CONSTANTS
import unittest


class BaseTestCase(object):

    def setUp(self):
        if TT_CONSTANTS['Browser'].lower() == 'firefox':
            print "I am Firefox"
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif TT_CONSTANTS['Browser'].lower() == 'chrome':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif TT_CONSTANTS['Browser'].lower() == 'ie':
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
        else:
            raise Exception("This browser is not supported at the moment.")

    def navigate_to_page(self, url):
        self.driver.get(url)

    def tearDown(self):
        print "Say Goodbye"
        self.driver.quit()


