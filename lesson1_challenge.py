from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="\\Users\\lngsvakti\\Desktop\\MyDocuments\\chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.amazon.com/s?k=lego")
lego_li = driver.find_elements(By.CSS_SELECTOR,
"div[class='s-main-slot s-result-list s-search-results sg-row'] span[data-component-type='s-product-image'] img ")
lego_first = lego_li[0]
print(lego_first.get_attribute("alt"))
lego_first.click()
