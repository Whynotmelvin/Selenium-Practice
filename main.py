from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your actual Instagram username and password
username = "Melvin.aj"
password = "Sophia2.0"

driver = webdriver.Chrome()

# Open Instagram
driver.get("https://www.instagram.com/")


# Find the username and password fields and fill them in
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")

username_field.send_keys(username)
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for some time to see the result (replace with actual wait strategies)
time.sleep(5)

# Close the browser
driver.quit()
