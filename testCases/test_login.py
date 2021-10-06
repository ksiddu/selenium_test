import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
# https://www.youtube.com/watch?v=57pjD89IFXA
# SDET- Automation Techie
# PAVAN KUMAR : POM Video
class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"
    screenshot_path ="./Screenshots"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title=="Your store. Login1":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screenshot_path + "/test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screenshot_path + "/test_login.png")
            self.driver.close()
            assert False