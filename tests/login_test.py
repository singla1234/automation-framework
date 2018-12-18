from selenium import webdriver
from pages.homepage import homepage
from pages.loginpage import loginpage
from utils import utils as utils
from pytest import fixture
import allure
import pytest

class Testlogin:
    @fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/gur29899/PycharmProjects/automation-framework/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")
    def test_login(self,test_setup):
        driver.get(utils.URL)
        login=loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()


    def test_logout(self,test_setup):
        try:
            home=homepage(driver)
            home.click_admin()
            home.click_logout()
            x=driver.title
            assert x=="OrangeHRM"
        except AssertionError as error:
            print("assertion error occureed")
            print(error)
            allure.attach(driver.get_screenshot_as_png(),name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("this is exception")
            raise
        else:
            print("no exception occurred")
        finally:
            print("i am inside finally block")

