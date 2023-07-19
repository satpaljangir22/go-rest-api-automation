Feature: Get User details

  Scenario: Verify All the users in response
    When Get call for all user is requested
    Then All users should be returned in the response

  Scenario: Verify user in response with user_id
    When Get call for user_id is requested
    Then User with user_id should be returned in the response