import unittest
from selenium.webdriver.common.by import By

import Utilities.BrowserConfiguration
from Utilities.BrowserConfiguration import setUp
from Utilities.Logger import Logger
from Utilities.Singleton import Singleton

base_url = "https://www.amazon.in/"
class TestAmazon(unittest.TestCase):
    driver = Singleton().instance.driver
    logger = Logger.loggen()

    def testcase001(self):
        self.logger.info("**********TC 001*********")
        self.driver.get("https://www.amazon.in/")
        self.driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("iphone")
        self.logger.info("*******************")

    def testcase002(self):
        self.logger.info("**********TC 002*********")
        self.driver.get("https://www.amazon.in/")
        self.driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("iphone")
        self.logger.info("*******************")

    def testcase003(self):
        self.logger.info("**********TC 003*********")
        self.driver.get("https://www.amazon.in/")
        self.driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("iphone")
        self.logger.info("*******************")


    def testcase004(self):
        self.logger.info("**********TC 004*********")
        self.driver.get("https://www.amazon.in/")
        self.driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("iphone")
        self.logger.info("*******************")



