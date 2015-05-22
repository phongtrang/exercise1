__author__ = 'phongtrinh'
import unittest
from selenium import webdriver
from pack.Login import *

class Test_logout(unittest.TestCase, Login):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = 'https://google.com'

    def test_click(self):
        session = Login(self.driver,self.url)
        session.login()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()