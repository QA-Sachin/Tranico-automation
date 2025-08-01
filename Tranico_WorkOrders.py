import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://tranico.imaxims.com/work-orders")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click login
login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/form/div[2]/button")))
login.click()

work_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[1]/div[2]/div[3]/p"))).click()

Add_work_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[1]/div[2]/a/button"))).click()

Select_customer = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select Customer']"))).click()

Select_customer_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Rahul']"))).click()

time.sleep(3)

machine = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'rizzui-select-button')]//span[text()='Select Machine']"))).click()

Select_machine = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id,'headlessui-listbox-option') and @role='option']"))).click()

issue_title = wait.until(EC.element_to_be_clickable((By.NAME, "issue_title"))).send_keys("machine not working")

issue_description = wait.until(EC.element_to_be_clickable((By.NAME, "issue_description"))).send_keys("This is test description Please ignore it")

time.sleep(12)

# File_upload = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div/div/div/div/button")))
#
# time.sleep(5)
#
# File_upload.send_keys("/Users/netmaximstechnologies/Downloads/intelelectric-logo.png")

priority = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[4]/div/div/div/button[1]"))).click()

time.sleep(2)

Save_work_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div[2]/div[2]/div/div[4]/div/div/button"))).click()

time.sleep(2)