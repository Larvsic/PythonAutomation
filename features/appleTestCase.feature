@firstTest
#Initial test to try framework working as expected using python and Selenium webdriver (Chrome)
Feature: Launch Apple page and scroll down
    Scenario: Scroll down
        Given As a user I launch "Apple" website
        When I see logo image displayed
        Then I scroll down

