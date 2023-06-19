from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


options = Options()
#options.add_argument('--headless')
driver=webdriver.Chrome(options)

driver.get('https://www.jumia.co.ke/')
driver.maximize_window()
driver.implicitly_wait(0.5)

dismiss_button = driver.find_element(by=By.XPATH, value='//*[@id="pop"]/div/section/button')
dismiss_button.click()

search_box = driver.find_element(by=By.NAME, value="q")
search_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

search_box.send_keys("Sneakers")
driver.implicitly_wait(0.5)
search_button.click()

window_after = driver.window_handles[0]
driver.switch_to.window(window_after)

item_card = driver.find_elements(By.CLASS_NAME, 'prd')

#for item in item_card:
#    item_name = item.find_element(By.CLASS_NAME, 'name')
#    item_price = item.find_element(By.CLASS_NAME, 'prc')
#    print(f"{item_name.get_attribute('innerHTML')}: {item_price.get_attribute('innerHTML')}")

print(driver.get_cookies())
