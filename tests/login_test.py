from selenium import webdriver
from pages.homepage import homepage
from pages.loginpage import loginpage
from utils import utils as utils
from pytest import fixture

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
        home=homepage(driver)
        home.click_admin()
        home.click_logout()
