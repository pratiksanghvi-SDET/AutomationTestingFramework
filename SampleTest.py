from sudo_pip_install import *
from importFiles import *


options = Options()
options.add_argument("start-maximized")
service_obj = Service("WebDrivers_path\chromedriver.exe")

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').send_keys('Narendra Modi')