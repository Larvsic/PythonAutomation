from selenium.webdriver.common.by import By
from browser import Browser


class InsidePageLocator(object):

    # Home Page Locators
    myNotes = (By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[2]/a")


class InsidePage(Browser):
    # Inside web page actions

    def get_page_title(self):
        return self.driver.title
