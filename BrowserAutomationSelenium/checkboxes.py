import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)
driver.get("https://www.keynotesupport.com/"
"internet/web-contact-form-example-checkboxes.shtml"
)

# -- Wait until the page loads - with implicit wait
driver.implicitly_wait(10)

# -- Finding all the input boxes at one time
input_boxes = driver.find_elements_by_class_name("data-entry")
"""
Unfortunately, we do not see any elements so have to scroll
down to see the first input box"""
subject_label = driver.find_element_by_css_selector(
    "#align > label:nth-child(5)"
)
driver.execute_script("arguments[0].scrollIntoView();", subject_label)

# -- Specifying the names of all text boxes
subject = input_boxes[0]
name = input_boxes[1]
phone = input_boxes[2]
email = input_boxes[3]

# -- Filling the text boxes
subject.send_keys("Data Science")
name.send_keys("James")
phone.send_keys("+1234567890")
email.send_keys("james.bond@email.com")

# -- Choosing checkboxes
desktop = driver.find_element_by_xpath(
    "//*[@id='align']/span[5]/input"
)
notebook = driver.find_element_by_xpath(
    "//*[@id='align']/span[6]/input"
)

# -- Testing our checkboxes are not selected
print(
    "Desktop is enabled but not selected yet: ",
    desktop.is_enabled() and not desktop.is_selected()
)
print(
    "Notebook is enabled but not selected yet: ",
    notebook.is_enabled() and not notebook.is_selected()
)

# -- Clicking on our checkboxes
desktop.click()
notebook.click()

# -- Testing our checkboxes now
print(
    "\nDesktop is enabled and selected: ",
    desktop.is_enabled() and desktop.is_selected()
)
print(
    "Notebook is enabled and selected: ",
    notebook.is_enabled() and notebook.is_selected()
)

"""We are going to clear all the data by pressing
the "Reset" button. Now we will store the value
of the "NAME" input box in a separate variable
to compare after clearing."""
name_value = name.get_attribute("value")

# -- Waiting for the user to read text boxes
time.sleep(5)

# -- Clicking on the reset button
reset = driver.find_element_by_css_selector(
    "#align > span:nth-child(38) > input:nth-child(1)"
)
reset.click()

# -- Finding a new value of "NAME"
new_value = name.get_attribute("value")

# -- Check if a new value is an empty string
print(
    "New value is an empty string: ",
    not new_value
)

driver.quit()
