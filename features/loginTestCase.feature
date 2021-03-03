@login
Feature: Log in
    Scenario: Log in
        Given I launch "http://testapp.galenframework.com/"
        When I click login button
        When I enter username and password
        Then I log in
        Then I validate im logged