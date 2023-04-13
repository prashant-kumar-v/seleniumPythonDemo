Feature: Login functionality

  Scenario: User logs in with valid credentials
    Given the login page is displayed
    When the user enters valid username and password
    And clicks on the login button
    Then the user should be logged in
