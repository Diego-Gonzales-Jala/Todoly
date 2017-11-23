@userFeature
Feature: User
This feature will be used to get, edit, delete and create new users
  @getuser @smoke
  Scenario: Get user information
	Given I have a service for "/user.json" for user
	When I send GET user request to get user information
	Then I receive status code 200 for the response

  @createUser @crud
  Scenario: Create user
    Given I have a service for "/user.json" to create user
	And I have create request payload:
	"""
      {"Email":"test.testingmb@jalasoft.com", "FullName": "Irina Torrico", "Password": "123456"}
    """
    When I send a POST request to create a new user
	Then I receive status code 200 for the response create user

  @updateUser @crud
  Scenario: Update User
      Given I have a service for "/user/0.json"
      And I have a payload to update:
	"""
      {"FullName": "diego test"}
    """
      When I send PUT user update request to update user in database
      Then I receive status code 200 for the response after update

  @deleteUser @crud
  Scenario: Delete User
      Given I have a service for "/user/0.json" to delete a user
      When I send DELETE items request to delete an exsiting user
      Then I receive status code 200 for the response after delete


