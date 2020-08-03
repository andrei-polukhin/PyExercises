import time
from selenium import webdriver

# Chrome
driver = webdriver.Chrome(
    executable_path="BrowserAutomationSelenium/chromedriver"
)

driver.get("http://demo.automationtesting.in/Windows.html")
element = driver.find_element_by_xpath("//*[@id='Tabbed']/p")
element_text = element.text
print(element_text)

time.sleep(5)
driver.get("https://github.com/tecladocode/complete-python-course")
driver.back()
driver.forward()
time.sleep(5)
driver.quit()
