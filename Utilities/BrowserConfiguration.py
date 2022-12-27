import selenium.webdriver.firefox.options
from selenium.common import WebDriverException
from selenium.webdriver.common.service import logger
import Utilities
from Utilities.ConfigurationFileReader import configurationFileReader
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as _firefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

# ---------------------------------------------------------------------------
maindriver = None


def getChromeDriver():
    op = Options()
    chromedriverPath = configurationFileReader.getPropertyValue('chromedriverPath')
    print('Browser Path set to', chromedriverPath)
    op.add_argument("start-maximized");
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
    maindriver = driver
    return maindriver


def getFirefoxDriver():
    op = _firefoxOptions()
    firefoxdriverPath = configurationFileReader.getPropertyValue('firefoxdriverPath')
    print('Browser Path set to', firefoxdriverPath)
    # op.add_argument("start-maximized");
    # op.add_experimental_option("excludeSwitches", ["enable-automation"])
    # op.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=op)
    maindriver = driver
    return maindriver


class BrowserConfiguration:
    browserName = configurationFileReader.getPropertyValue('browserName')
    print('Browser Name set to', browserName)

    if browserName.lower() == 'chrome':
        driver = getChromeDriver()
    elif browserName.lower() == 'firefox':
        driver = getFirefoxDriver()

    url = "https://www.google.com/"
    url = url.encode('ascii', 'ignore').decode('unicode_escape')

    driver.get(url)
