from selenium import webdriver
from configuration.elements import obj
from selenium.webdriver.chrome.options import Options


class Browser(object):

    options = Options()
    options.add_argument(obj.disable_notification)
    context.driver = webdriver.Chrome(
        executable_path=obj.chromePath, chrome_options=options)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

    def close(self, context):
        context.driver.close()
