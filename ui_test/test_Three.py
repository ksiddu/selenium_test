import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = None

@pytest.fixture
def setup():
    print("Driver init")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    print("Driver cleanup")
    driver.close()
    driver.quit()

@pytest.mark.smoke
def test_1(setup):
    print("Test Starts")
    driver.get("https://www.facebook.com")
    expected_title = "Facebook – log in or sign up"
    actual_title = driver.title
    print("actual_title", actual_title)
    print("expected_title", actual_title)
    assert actual_title == expected_title
    sleep(1)


@pytest.mark.regression
def test_2(setup):
    print("Test Starts")
    driver.get("https://www.google.com")
    expected_title = "Google"
    actual_title = driver.title
    print("actual_title", actual_title)
    print("expected_title", actual_title)
    assert actual_title == expected_title
    sleep(1)


@pytest.mark.smoke
def test_3(setup):
    print("Test Starts")
    driver.get("https://www.yahoo.com")
    expected_title = "Yahoo Singapore | News, Finance and Lifestyle"
    actual_title = driver.title
    print("actual_title", actual_title)
    print("expected_title", actual_title)
    assert actual_title == expected_title
    sleep(1)

# commands to run using pytest and markers
# pytest ui_test/test_Second.py -rA --junitxml=index.xml
# pytest ui_test/test_Three.py -rA --junitxml=MyXmlReport3.xml --html=MyHtmlReport3.html -m smoke