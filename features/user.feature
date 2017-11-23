@userFeature
Feature: User
User feature
  @getuser @smoke
  Scenario: Get user information
	Given I have a service for "/user.json" for user
	When I send GET user request to get user information
	Then I receive status code 200 for the response



  @createUser @crud
  Scenario: Create user
    Given I have a service for "/user.json"
	And I have create request payload:
	"""
      {
        "Email":"test.testi@jalasoft.com"
	 	"FullName": "Irina Torrico"
	 	"Password": "123456"
      }
    """
    When I send a POST request to create a new user
	Then I receive status code 200 for the response create user