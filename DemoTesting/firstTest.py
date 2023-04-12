cloud_url = 'http://192.168.23.74:30004/wd/hub'

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

options.browser_version = '111.0'
cloud_options = {
    'name': 'Demoqa',
    'enableLogs': True,
    'enableVideo': True,
    'deviceName': 'Desktop',
    'screenResolution': '1366x768x24',
    'timeout': 60,
    'idleSessionTimeout': 60,
}
options.set_capability('cloudify:options', cloud_options)

driver = webdriver.Remote(cloud_url, options=options)


# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)


def fill_details_by_id(locator, value):
    driver.find_element(By.ID, locator).send_keys(value)


fill_details_by_id("userName", "Rahul")
fill_details_by_id("userEmail", "rahul.k@gmail.com")
fill_details_by_id("currentAddress", "Sector 15, Noida")
fill_details_by_id("permanentAddress", "Hauz Khas, Delhi")
submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
# print(submit.text)
submit.click()
# wait = WebDriverWait(driver, 10, poll_frequency=2)
# submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#submit")))

# Assertions
# print(driver.find_element(By.ID, "name").text)
time.sleep(4)
# driver.close()
driver.quit()
