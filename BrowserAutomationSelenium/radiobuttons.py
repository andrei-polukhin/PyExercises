import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)
driver.get(
    "https://www.keynotesupport.com/internet/"
    "web-contact-form-example-radio-buttons.shtml"
)
# -- Wait until the page loads - with implicit wait
driver.implicitly_wait(10)

# -- Finding all the input boxes at one time
input_boxes = driver.find_elements_by_class_name("data-entry")
"""Unfortunately, we do not see any elements so have to scroll
down to see the first input box"""
name_label = driver.find_element_by_css_selector(
    "#align > label:nth-child(7)"
)
driver.execute_script("arguments[0].scrollIntoView();", name_label)

# -- Specifying the names of all text boxes
name = input_boxes[0]
phone = input_boxes[1]
email = input_boxes[2]

# -- Sending data
name.send_keys("James")
phone.send_keys("+1234567890")
email.send_keys("james.bond@email.com")

# -- Finding radio buttons
software_product = driver.find_element_by_xpath(
    "//*[@id='align']/span[7]/input"
)
level = driver.find_element_by_css_selector(
    "#align > span:nth-child(39) > input[type=radio]"
)

# -- Clicking on the software button
software_product.click()

# -- Scrolling down to the level button
driver.execute_script("arguments[0].scrollIntoView();", level)

# -- Clicking on the level button
level.click()

# -- Checking if the radio buttons are selected
print("Software product is selected: ", software_product.is_selected())
print("Current level is selected: ", level.is_selected())

# -- Finding textarea and sending the comment
comments = driver.find_element_by_id("comments3")
comments.send_keys("Written using Selenium in Python :)")

# -- Wait until the user can read what we have done :)
time.sleep(8)

# -- Finding and clicking on the submit button
submit = driver.find_element_by_xpath("//*[@id='align']/span[12]/input[2]")
submit.click()

# -- Waiting for the new page to load
time.sleep(5)

driver.quit()
