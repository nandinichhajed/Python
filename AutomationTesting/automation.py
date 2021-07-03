from selenium import webdriver
chrome_browser = webdriver.Chrome(executable_path = "./chromedriver.exe")
# To open chrome window
# print(chrome_browser)
# chrome_browser.maximize_window()
# chrome_browser

# Basics 1
chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('Selinium Easy Demo' in chrome_browser.title)
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

# Basics 2
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id(user_message)
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM EXTRA COOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'I AM EXTRA COOOL' in output_message.text

# Basics 3
chrome_browser.close()  # for a single window to be closed
chrome_browser.quit()  # for the entire windows to be closed
