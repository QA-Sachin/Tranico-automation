import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://tranico.imaxims.com/customers")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click login
login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/form/div[2]/button")))
login.click()

Customers = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[2]"))).click()

Add_customer = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[1]/div[2]/a/button"))).click()

site_name = wait.until(EC.element_to_be_clickable((By.NAME, "site_name"))).send_keys("Rahul")

site_number = wait.until(EC.element_to_be_clickable((By.NAME, "site_number"))).send_keys("SA87675")

address = wait.until(EC.element_to_be_clickable((By.NAME, "address"))).send_keys("New town, Canada")

postcode = wait.until(EC.element_to_be_clickable((By.NAME, "postcode"))).send_keys("SW1A1AA")

Contact = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.0.name"))).send_keys("Prem Jeevan")

phone = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.0.phone"))).send_keys("07896523651")

Email = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.0.email"))).send_keys("sachinchauhan.netmaxims+87@gmail.com")

Add_conatct = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[3]/div[1]/button"))).click()

Contact_1 = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.1.name"))).send_keys("Amar Jeevan")

phone_1 = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.1.phone"))).send_keys("07896523656")

Email_1 = wait.until(EC.element_to_be_clickable((By.NAME, "contacts.1.email"))).send_keys("sachinchauhan.netmaxims+81@gmail.com")


Save_Customer = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[4]/div/div/div/button"))).click()


time.sleep(3)