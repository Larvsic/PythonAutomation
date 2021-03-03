"""
Import Section 
"""
import requests
import json
from behave import then
from selenium import webdriver
from configuration.configurationFile import *
from configuration.urlFiles import *
from configuration.elements import *
from selenium.webdriver.common.keys import Keys
from configuration.elements import obj


# API Testing


# Front End Testing
@then(u'I close browser')
def closeBrowser(context):
    context.driver.quit()


@then(u'I verify airpodsmax is displayed')
def isDisplayed(context):
    context.driver.find_elements_by_xpath(obj.airpodsMax).is_displayed()


@then(u'I log in')
def login(context):
    context.driver.find_element_by_xpath(obj.loginButton2).click()


@then(u'I validate im logged')
def validation(context):
    element = context.driver.find_element_by_xpath(obj.myNotes).text
    assert element == 'My Notes'
