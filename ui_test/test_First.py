from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = None
def setUp():
    print("Driver init")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

def test_1():
    print("Test Starts")
    driver.get("https://www.facebook.com")
    expected_title = "Facebook – log in or sign up"
    actual_title = driver.title
    print("actual_title", actual_title)
    #assert expected_title is actual_title
    print("Test Completes")

def tearDown():
    print("Driver clean up")
    driver.close()
    driver.quit()

setUp()
test_1()
tearDown()
