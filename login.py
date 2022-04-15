from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://syncnau.poltektegal.ac.id/login")
##Valid
#driver.find_element_by_name("username").send_keys("19090034")
#driver.find_element_by_id("password").send_keys("password")
#driver.find_element_by_id("submit").click()

##Invalid
driver.find_element_by_name("username").send_keys("19090034")
driver.find_element_by_id("password").send_keys("yoga12345")
driver.find_element_by_id("submit").click()