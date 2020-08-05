import time

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)
driver.get("https://www.webpagetest.org/")

# -- Press the login button on the main page
main_login = driver.find_element_by_xpath("//*[@id='wptAuthBar']/a[1]")
main_login.click()

# -- Wait until the page is loaded
driver.implicitly_wait(5)

# -- Find username and password boxes, and the submit button
login_box = driver.find_element_by_name("username")
password_box = driver.find_element_by_name("password")
submit_button = driver.find_element_by_name("submit")

# -- Sending credentials
login_box.send_keys("retromobile2457")
password_box.send_keys("asdflgslkasdwegau876597")
submit_button.click()

# -- Quitting
time.sleep(5)
"""
The difference between time.sleep and driver.implicitly_wait
is that time.sleep delays executing a programme for a specific
amount of time, while for explicitly_wait - we wait UP TO this
number of seconds until the previous command is being executed.
"""
driver.quit()
