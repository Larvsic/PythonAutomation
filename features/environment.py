import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configuration.elements import obj
from browser import Browser
from pages.insidePage import InsidePage
from pages.loginLandingPage import LoginLandingPage
from pages.loginPage import LoginPage


def before_all(context):
    print("before all")
    context.browser = Browser()
    context.insidePage = InsidePage()
    context.loginLandingPage = LoginLandingPage()
    context.loginPage = LoginPage()


def after_all(context):
    pass
    # context.driver.quit()
