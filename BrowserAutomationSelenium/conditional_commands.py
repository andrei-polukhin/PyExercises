import time
import getpass

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

# -- For the sake of running silently
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('window-size=1200x600')
# -- Specifying the path to the webdriver and the URL
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver", options=options
)
driver.get("https://mergify.io/")

# -- Checking the sign up button
sign_up = driver.find_element_by_xpath("//*[@id='headerNav']/div[3]/a[2]")
print("Sign up is displayed on the main page: ", sign_up.is_displayed())
print("Sign up is enabled on the main page: ", sign_up.is_enabled())

# -- Clicking on the login button on the main page
login_button = driver.find_element_by_xpath("//*[@id='headerNav']/div[3]/a[1]")
login_button.click()

# -- Testing non-existent credentials on GitHub
login = driver.find_element_by_id("login_field")
password = driver.find_element_by_name("password")
commit_button = driver.find_element_by_name("commit")
print("GitHub commit button is enabled: ", commit_button.is_enabled())

# -- Entering data and 'pressing' the commit button
login_input = input("\nEnter your GitHub username: ")
password_input = getpass.getpass()

login.send_keys(login_input)
password.send_keys(password_input)
commit_button.click()

# -- Test if the code not succeeded
try:
    # -- This block will be found only if the credentials are wrong
    error = driver.find_element_by_id("js-flash-container")
except NoSuchElementException:
    # -- If the login succeeded, we are supposed to be redirected
    time.sleep(5)
    new_url = driver.current_url
    if new_url == "https://dashboard.mergify.io/installation":
        print("\nLogin successful!")
else:
    print("\nIncorrect credentials!")

driver.quit()
