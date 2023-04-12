import time

from selenium import webdriver
from selenium.webdriver.common.by import By

cloud_url = 'http://192.168.23.74:30004/wd/hub'

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.browser_version = '100.0'
cloud_options = {
    'name': 'FB create account',
    'enableLogs': True,
    'enableVideo': True,
    'deviceName': 'Desktop',
    'screenResolution': '1366x768x24',
    'timeout': 60,
    'idleSessionTimeout': 60,
}
options.set_capability('cloudify:options', cloud_options)

driver = webdriver.Remote(cloud_url, options=options)
# driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
# time.sleep(2)
driver.find_element(By.XPATH, '//*[@data-testid="open-registration-form-button"]').click()
# time.sleep(2)
driver.find_element(By.NAME, "firstname").send_keys("Ranbir")
driver.find_element(By.NAME, "lastname").send_keys("Kumar")
driver.find_element(By.NAME, "reg_email__").send_keys("ranbir.k@gmail.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("ranbir.k@gmail.com")
driver.find_element(By.NAME, "reg_passwd__").send_keys("ranbir@123")
# time.sleep(4)
