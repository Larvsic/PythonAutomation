from selenium.webdriver.common.by import By
from browser import Browser


class LoginLandingPageLocator(object):

    # Home Page Locators
    loginButton = (By.XPATH, "/html/body/div[2]/div[2]/div/div/p[3]/button")


class LoginLandingPage(Browser):
    # Login landing page actions
    def navigate(self, URLaddress):
        self.driver.get(URLaddress)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    # def fill(self, text, *locator):
    #     self.driver.find_element(*locator).send_keys(text)

    # def click_element(self, *locator):
    #     self.driver.find_element(*locator).click()

    # def navigate(self, address):
    #     self.driver.get(address)

    # def get_page_title(self):
    #     return self.driver.title

    # def search(self, search_term):
    #     self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
    #     self.click_element(*HomePageLocator.SUBMIT_BUTTON)
