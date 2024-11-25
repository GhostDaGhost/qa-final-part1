from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def FailedLogin():
    driver = webdriver.Chrome()
    driver.get("https://letsusedata.com")
    time.sleep(2)

    driver.find_element(By.ID, "txtUser").click()
    driver.find_element(By.ID, "txtUser").clear()
    driver.find_element(By.ID, "txtUser").send_keys("test1")
    driver.find_element(By.ID, "txtPassword").click()
    driver.find_element(By.ID, "txtPassword").clear()
    driver.find_element(By.ID, "txtPassword").send_keys("test1234")
    driver.find_element(By.ID, "javascriptLogin").click()
    
    # GIVE THE PAGE SOME TIME TO FULLY LOAD
    time.sleep(5)

# ON INITIALIZATION
FailedLogin()
