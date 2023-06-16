from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


options = Options()
options.add_argument('--headless')
driver=webdriver.Chrome(options)

driver.get('https://www.jumia.co.ke/')

driver.implicitly_wait(0.5)
flashsales=driver.find_element(By.CLASS_NAME,'-rad4')

flashsale_items = flashsales.find_elements(By.CLASS_NAME, 'itm')

for item in flashsale_items:
    price_item = driver.find_element(By.CLASS_NAME, 'prc')
    print(price_item)
