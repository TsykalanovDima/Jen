Feature: Sauce Demo
  Scenario: Sign in
    Given Open page
    When Open page
    And Enter username and password
    Then Click login button and assert
    And Quit browser