from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="\\Users\\lngsvakti\\Desktop\\MyDocuments\\chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://www.amazon.com/s?k=lego")
lego_first = driver.find_element(By.CSS_SELECTOR, "div[class='s-main-slot s-result-list s-search-results sg-row']>div:nth-child(2) div>a")
lego_first.click()
driver.quit()
