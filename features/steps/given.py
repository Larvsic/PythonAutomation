"""
Import Section
"""
import requests
import json
from behave import given
from selenium import webdriver
from configuration.configurationFile import *
from configuration.urlFiles import *


# API Testing


# Front End Testing
@given(u'As a user I launch "{URL}" website')
def OpenURL(context, URL):
    driver.get(URL)
    driver.implicitly_wait(2)
    # from configuration.endpoints import MockEndpoints
    # from data_dictionary.earlyValidation_data import *
