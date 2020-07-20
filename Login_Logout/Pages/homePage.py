from Login_Logout.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_xPath = Locators.logout_link_xPath

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xPath).click()
