import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configuration.elements import obj


def before_all(context):
    #context.driver = webdriver.Chrome(ChromePath)
    print("before all")
    options = Options()
    options.add_argument(obj.disable_notification)
    context.driver = webdriver.Chrome(
        executable_path=obj.chromePath, chrome_options=options)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


def after_all(context):
    pass
    # context.driver.quit()
