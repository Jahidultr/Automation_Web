Feature: Login Functionality

  Scenario: Valid Login
    Given the user is on the login page
    When the user enters "test_user" and "password123"
    And clicks the login button
    Then the user should be redirected to the dashboard

  Scenario: Invalid Login
    Given the user is on the login page
    When the user enters "wrong_user" and "wrong_password"
    And clicks the login button
    Then an "Invalid credentials" error should be displayed
