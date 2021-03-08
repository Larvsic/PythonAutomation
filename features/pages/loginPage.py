from selenium.webdriver.common.by import By
from browser import Browser


class LoginPageLocator(object):

    # Home Page Locators
    txtbox_userName = (By.XPATH, "/html/body/div[2]/div[2]/div/div/p[1]/input")
    txtbox_password = (By.XPATH, "/html/body/div[2]/div[2]/div/div/p[2]/input")
    loginButton2 = (
        By.XPATH, "/html/body/div[2]/div[2]/div/div/p[3]/button[1]")


class LoginPage(Browser):
    # Login landing page actions
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
