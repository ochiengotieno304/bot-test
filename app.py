from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--headless')
driver=webdriver.Chrome(options)

driver.get('https://www.jumia.co.ke/')
cookies = driver.get_cookies()
saved_cookies = []
for cookie in cookies:
    saved_cookies.append(cookie)

driver.maximize_window()
driver.implicitly_wait(0.5)

dismiss_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/button')
dismiss_button.click()

search_box = driver.find_element(By.XPATH,'//*[@id="fi-q"]')
search_button = driver.find_element(By.XPATH, '//*[@id="search"]/button')

search_box.send_keys("sneakers")
search_button.click()
driver.implicitly_wait(0.5)

#while True:
#    for cookie in saved_cookies:
#        driver.add_cookie(cookie)
#        
#    item_card = driver.find_elements(By.CLASS_NAME, 'prd')
#    
#    for item in item_card:
#        item_name = item.find_element(By.CLASS_NAME, 'name')
#      item_price = item.find_element(By.CLASS_NAME, 'prc')
#       print(f"{item_name.get_attribute('innerHTML')}: {item_price.get_attribute('innerHTML')}")
#    next_button = driver.find_element(By.XPATH, '//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[6]')
#    if not next_button.is_enabled():
#        break
#    next_button.click()
#print(driver.get_cookies())
