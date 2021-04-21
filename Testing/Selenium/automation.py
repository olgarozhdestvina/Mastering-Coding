# Testing on Selenium Easy
# need to add waits to simulate human actions

from selenium import webdriver

# Create an instance of a browser
chrome_browser = webdriver.Chrome('chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# If not found, assertion error will come up
assert 'Selenium Easy Demo' in chrome_browser.title

# Through the selector
button = chrome_browser.find_element_by_class_name('btn-default')
button_text = button.get_attribute('innerHTML')

# Type the message into the box
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('HELLOOOO')


# Click the button and display the text
button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'HELLOOOO' in output_message.text

# Grab all elements with ID get input that are a child of class btn
#all_buttons = chrome_browser.find_element_by_css_selector('#get-input > .btn')

chrome_browser.close() # sometimes need to close twice
chrome_browser.quit() # quits all sessions