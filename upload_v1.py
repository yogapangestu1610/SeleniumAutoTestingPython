from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://syncnau.poltektegal.ac.id/profil")

driver.find_element_by_name("user_foto").send_keys("C:/Users/LENOVO/Downloads/UTS/BuFina/Selenium/foto_profil.png")
driver.find_element_by_name("simpan_foto").click()
