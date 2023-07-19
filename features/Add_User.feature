Feature: Add new user

  Scenario: Verify new user is added
    When Post call to add user is requested
    Then User details should be returned in the response