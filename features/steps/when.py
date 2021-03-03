"""
Import Section
"""
import requests
import json
from behave import when
from selenium import webdriver
from configuration.configurationFile import *
from configuration.urlFiles import *
from selenium.webdriver.common.keys import Keys
from configuration.elements import obj


@when(u'I click login button')
def clickLogin(context):
    context.driver.find_element_by_xpath(obj.loginButton).click()


@when(u'I enter username and password')
def enterUserPass(context):
    context.driver.find_element_by_xpath(
        obj.txtbox_userName).send_keys(obj.userName)
    context.driver.find_element_by_xpath(
        obj.txtbox_password).send_keys(obj.password)
