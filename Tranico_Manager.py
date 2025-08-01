import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://tranico.imaxims.com/auth/login?returnTo=%2Fengineers")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click login
login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/form/div[2]/button")))
login.click()

# Click Engineers
Engineers = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[1]/p")))
Engineers.click()

# Click Add Engineer
Add_Engineer = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/button")))
Add_Engineer.click()

# Fill Name
Contact_name = wait.until(EC.presence_of_element_located((By.NAME, "name")))
Contact_name.send_keys("Ravi Sharma")

# Fill Email
email = driver.find_element(By.NAME, "email")
email.send_keys("sachinchauhan.netmaxims+57@gmail.com")

# Fill Phone
phone = driver.find_element(By.NAME, "phone")
phone.send_keys("07896523659")


work_area = driver.find_element(By.XPATH, "//input[@placeholder='SW1A 1AA']").click()

time.sleep(3)

work_area = driver.find_element(By.XPATH, "//input[@placeholder='SW1A 1AA']")
work_area.send_keys("SW1A 1AA", Keys.ENTER)

# Click Save
save_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
save_button.click()

print("Engineer added successfully!")



