from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import json

firefox_driver_path = '<path_geckodriver>'
s = Service(firefox_driver_path)
browser = webdriver.Firefox(service=s)

url = "https://github.com/search?o=desc&q=access_key&s=indexed&type=Code"
browser.get(url)

email = browser.find_element("id", "login_field")
email.send_keys("<email>")
password = browser.find_element("id", "password")
password.send_keys("<password>")
password.send_keys(Keys.RETURN)
time.sleep(10)

for i in range(15):
    results = browser.find_elements(By.CSS_SELECTOR, '.code-list-item')
    for result in results:
        lines = result.text.splitlines()
        for i, line in enumerate(lines):
            match = re.search(r"access_key", line)
            if match:
                url_data = result.find_elements(By.CSS_SELECTOR, "[data-hydro-click]")
                for url_item in url_data:
                    data = json.loads(url_item.get_attribute('data-hydro-click'))
                    url = data["payload"]["result"]["url"]
                    print(line)
                    print(url)
    browser.find_element(By.CSS_SELECTOR, '.next_page').click()
    time.sleep(10)
