import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "/home/garv/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://127.0.0.1:8000/")



time.sleep(2)
signup = driver.find_element(By.XPATH, '/html/body/nav/div/a[3]')
signup.click()

time.sleep(2)
username = driver.find_element(By.XPATH, '//*[@id="id_username"]')
username.send_keys("garv312")

email = driver.find_element(By.XPATH, '//*[@id="id_email"]')
email.send_keys("garvy312@gmail.com")

password = driver.find_element(By.XPATH, '//*[@id="id_password1"]')
password.send_keys('MSIlaptop@1')

repassword = driver.find_element(By.XPATH, '//*[@id="id_password2"]')
repassword.send_keys('MSIlaptop@1')

time.sleep(2)
submit = driver.find_element(By.XPATH, '/html/body/div/div/form/button')
submit.click()


login = driver.find_element(By.XPATH, '//*[@id="id_username"]')
login.send_keys("garv312")
passwordd = driver.find_element(By.XPATH, '//*[@id="id_password"]')
passwordd.send_keys("MSIlaptop@1")
time.sleep(200)


