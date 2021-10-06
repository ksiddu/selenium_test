from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

# test application: https://rahulshettyacademy.com/AutomationPractice/
# https://medium.com/nerd-for-tech/browser-automation-with-python-and-selenium-12-managing-alerts-47c0b85cee81

driver = None

def setUp():
    print("Driver init")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

def tearDown():
    print("Driver clean up")
    driver.close()
    driver.quit()

# just ok button
def testJavascriptSimpleAlert():
    app_url = "https://rahulshettyacademy.com/AutomationPractice/"
    driver.get(app_url)
    sleep(2)
    input_box = driver.find_element_by_css_selector("#name")
    alert_button = driver.find_element_by_css_selector("#alertbtn")
    expected_text = "Siddu"
    input_box.send_keys(expected_text)
    alert_button.click()
    # alert = driver.switch_to_alert
    # create alert object
    alert = Alert(driver)
    sleep(2)
    actual_text = alert.text
    print(f"Alert text: {alert.text}")
    assert expected_text in actual_text
    print(alert.text)
    alert.accept()

# ok and cancel buttons
def testJavascriptConfirmAlert():
    app_url = "https://rahulshettyacademy.com/AutomationPractice/"
    driver.get(app_url)
    sleep(2)
    input_box = driver.find_element_by_css_selector("#name")
    confirm_button = driver.find_element_by_css_selector("#confirmbtn")
    expected_text = "Siddu"
    input_box.send_keys(expected_text)
    confirm_button.click()
    # alert = driver.switch_to_alert
    # create alert object
    alert = Alert(driver)
    sleep(2)
    actual_text = alert.text
    print(f"Alert text: {alert.text}")
    assert expected_text in actual_text
    print(alert.text)
    alert.accept()

setUp()
#testJavascriptSimpleAlert()
testJavascriptConfirmAlert()
tearDown()