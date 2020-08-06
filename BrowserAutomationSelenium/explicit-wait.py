import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)
driver.get("https://avia.tickets.ua/en")

# -- Specifying explicit wait
wait = WebDriverWait(driver, 10)

# -- Clicking on the flights&hotels button
flights_and_hotel = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/header/div[4]/section/nav/ul/li[6]/button")
    )
)
flights_and_hotel.click()

# -- Closing the first tab
driver.switch_to.window(driver.window_handles[0])
driver.close()
time.sleep(2)  # just for playing safe
# -- Switching the focus to the new tab
driver.switch_to_window(driver.window_handles[0])

# -- Choosing departure and sending the city name
departure = driver.find_element(By.ID, "from_name")
departure.clear()
departure.send_keys("Kyiv")

# -- Choosing arrival and sending the city name
arrival = driver.find_element_by_id("to_name")
arrival.clear()
arrival.send_keys("Istanbul")

# -- Clicking on the departure date button
departure_date = driver.find_element_by_id("departure_date")
departure_date.click()

# -- Choosing the next month for departure
next_month = driver.find_element_by_xpath(
    "//*[@id='ui-datepicker-div']/div[2]/div/a"
)
next_month.click()

# -- Choosing the departure date
exact_date = driver.find_element_by_xpath(
    "//*[@id='ui-datepicker-div']/div[2]/table/tbody/tr[2]/td[5]/a"
)
exact_date.click()
time.sleep(2)  # until the new JS window opens

# -- Choosing the arrival date
arrival_date = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[4]/td[1]/a")
    )
)
arrival_date.click()

# -- Pressing the final search button
search_button = driver.find_element_by_xpath(
    "//*[@id='avia-hotel']/div/form/div[2]/div/div[1]/div/input"
)
search_button.click()

"""
WARNING: this works as for 2020-08-05
"""
time.sleep(8)
driver.quit()
