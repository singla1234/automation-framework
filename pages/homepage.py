class homepage:
    def __init__(self,driver):
        self.driver=driver
        self.admin_button="user-dropdown"
        self.logout_button="logoutLink"

    def click_admin(self):
        self.driver.find_element_by_id(self.admin_button).click()
    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button).click()