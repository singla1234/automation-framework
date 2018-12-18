import pytest
@pytest.fixture(scope="class")

def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/gur29899/PycharmProjects/automation-framework/drivers/chromedriver.exe")
    print(driver)
    driver.implicitly_wait(5)
    request.cls.driver=driver
    yield
    driver.close()
    driver.maximize_window()
    driver.quit()
    print("Test Completed")