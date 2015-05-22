__author__ = 'phongtrinh'
from pack.Login import *
import unittest
from selenium import webdriver

class Test(unittest.TestCase, Login):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.url = 'https://google.com'

    def test(self):
        session = Login(self.driver,self.url)
        session.click()
        session.login()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
