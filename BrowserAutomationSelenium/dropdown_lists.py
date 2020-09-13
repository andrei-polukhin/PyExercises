import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)
driver.get("https://form.jotform.com/202193179323352")

# -- Specifying the country (dropdown list)
country = driver.find_element_by_css_selector(
    "#input_92_country"
)

# -- Scrolling to the element
driver.execute_script("arguments[0].scrollIntoView();", country)

# -- Selecting "Ukraine" by value
drp_country = Select(country)
drp_country.select_by_value("Ukraine")

# -- Finding the student's birth information
birth_month = driver.find_element_by_id(
    "input_95_month"
)
birth_day = driver.find_element_by_id(
    "input_95_day"
)
birth_year = driver.find_element_by_id(
    "input_95_year"
)

# -- Specifying dropdowns
drp_month = Select(birth_month)
drp_day = Select(birth_day)
drp_year = Select(birth_year)

# -- Using dropdowns
drp_month.select_by_visible_text("August")
drp_day.select_by_visible_text("17")
drp_year.select_by_visible_text("1980")

time.sleep(4)
driver.quit()
