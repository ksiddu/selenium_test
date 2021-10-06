#Implicit wait
#Explicit wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# https://rahulshettyacademy.com/seleniumPractise/#/
def setUp():
    print("Driver init")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

def tearDown():
    print("Driver clean up")
    driver.close()
    driver.quit()

# ok and cancel buttons
def testSearchAndAddProducts():
    app_url = "https://rahulshettyacademy.com/seleniumPractise/#/"
    driver.get(app_url)
    sleep(2)
    input_box = driver.find_element_by_css_selector("[type='search']")
    submit_button = driver.find_element_by_css_selector("[type='submit']")
    expected_text = "ber"
    input_box.send_keys(expected_text)
    submit_button.click()
    products = driver.find_elements_by_xpath("//div[@class='products']/div[@class='product']")
    count = len(products)
    print(f"Products count: {len(products)}")
    assert count == 3
    buttons = driver.find_elements_by_xpath("//div[@class='products']/div[@class='product']/div[@class='product-action']")
    print(f"Buttons count: {len(buttons)}")
    for button in buttons:
        button.click()
        sleep(1)

    cart_button = driver.find_element_by_css_selector("[alt='Cart']")
    proceed_button = driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
    cart_button.click()
    proceed_button.click()
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
    promo_code = driver.find_element_by_css_selector("[class='promoCode']")
    apply_button = driver.find_element_by_css_selector("[class='promoBtn']")
    promo_code.send_keys("rahulshettyacademy")
    apply_button.click()
    wait = WebDriverWait(driver, 7)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
    promo_label = driver.find_element_by_css_selector("span.promoInfo")
    assert promo_label.is_displayed()
    print(f"Promo Message: {promo_label.text}")




setUp()
testSearchAndAddProducts()
tearDown()