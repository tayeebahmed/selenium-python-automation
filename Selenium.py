from sys import maxsize
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from websocket import send
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID))

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-button"))
).click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
).click()
driver.find_element(By.ID, "back-to-products").click()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
).click()

expected_url = "https://www.saucedemo.com/cart.html"
actual_url = driver.current_url

assert expected_url == actual_url, "cart page validate fail"
print("cart page validate success")
