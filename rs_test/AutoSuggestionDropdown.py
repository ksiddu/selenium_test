from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# test application: https://rahulshettyacademy.com/dropdownsPractise/

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

def testDropDownRun():
    app_url = "https://rahulshettyacademy.com/dropdownsPractise/"
    driver.get(app_url)
    sleep(2)
    driver.find_element_by_id("autosuggest").send_keys("ind")
    sleep(2)
    countries = driver.find_elements_by_css_selector("[class='ui-menu-item'] a")
    print(len(countries))
    for country in countries:
        if country.text == "India":
            country.click()
            sleep(2)
            actual = driver.find_element_by_id("autosuggest").get_attribute("value")
            print(actual)
            assert actual == "India"
            break



setUp()
testDropDownRun()
tearDown()
