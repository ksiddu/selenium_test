from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# test application: https://rahulshettyacademy.com/AutomationPractice/

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

def testAllCheckBoxesRun():
    app_url = "https://rahulshettyacademy.com/AutomationPractice/"
    driver.get(app_url)
    sleep(2)
    checkboxes = driver.find_elements_by_xpath("//*[@id='checkbox-example']//input[@type='checkbox']")
    print(len(checkboxes))
    for checkbox in checkboxes:
        checkbox.click()
        sleep(1)
        assert checkbox.is_selected()


def testSpecificCheckBoxeRun():
    app_url = "https://rahulshettyacademy.com/AutomationPractice/"
    driver.get(app_url)
    sleep(2)
    checkboxes = driver.find_elements_by_xpath("//*[@id='checkbox-example']//input[@type='checkbox']")
    print(len(checkboxes))
    option = "option2"
    sleep(2)
    for checkbox in checkboxes:
        value_attribute = checkbox.get_attribute("value")
        print(value_attribute)
        if value_attribute == option:
            checkbox.click()
            sleep(1)
            assert checkbox.is_selected()
            break




setUp()
#testAllCheckBoxesRun()
testSpecificCheckBoxeRun()
tearDown()
