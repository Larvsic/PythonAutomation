"""
Import Section 
"""
import requests
import json
from behave import then
from selenium import webdriver
from configuration.configurationFile import *
from configuration.urlFiles import *


# API Testing


# Front End Testing
@then(u'I close browser')
def closeBrowser(context):
    driver.quit()
