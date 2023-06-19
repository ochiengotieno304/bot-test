from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


options = Options()
options.add_argument('--headless')
driver=webdriver.Chrome(options)

driver.get('https://www.jumia.co.ke/')

driver.implicitly_wait(0.5)
item_card = driver.find_elements(By.CLASS_NAME, 'prd')

for item in item_card:
    item_name = item.find_element(By.CLASS_NAME, 'name')
    item_price = item.find_element(By.CLASS_NAME, 'prc')
    print(f"{item_name.get_attribute('innerHTML')}: {item_price.get_attribute('innerHTML')}")

