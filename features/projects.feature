@projectsFeature
Feature: Projects
As ToDo user
 I want to manage my projects
 Because Project holds a number of items. Every Item in the system belongs to a Project.
 If an Item doesn’t have a Project assigned to it, it only displayed in the Inbox.
 Projects can be in hierarchy containing other projects.

Background: User authenticated
    Given I have a new user authenticated
#******************GET method*************************
@smoke
Scenario: Get All Projects
 Given I have a service of "/projects.json"
 When I send "GET" project request
 Then I receive the status code "200" for the response

@smoke
Scenario: Get Project By Id
 Given I have a service of "/projects/3662858.json"
 When I send "GET" project request to see a proyect
 Then I receive the status code "200" for the response

@smoke
Scenario: Get Items of a Project
 Given I have a service of "/projects/3662858/items.json"
 When I send "GET" project request to see the items in a proyect
 Then I receive the status code "200" for the response


@smoke
Scenario: Get Done Items of a Project
 Given I have a service of "/projects/3662858/doneitems.json"
 When I send "GET" project request to see the done items in a proyect
 Then I receive the status code "200" for the response

#******************POST method*************************
@smoke
Scenario: Create New Project
 Given I have a service of "/projects.json"
 When I send "POST" project request with generic body.json
 """
 {
  "Content": "My New GenericProject-Alex",
  "Icon": 4
  }
 """
 Then I receive the status code "200" for the response

#******************PUT method*************************

@smoke
Scenario: Update Project By Id
 Given I have a service of "/projects/3662858.json"
 When I send "PUT" project request with generic body.json to update a proyect
 """
 {
 "Content": "My Update GenericProject-Alex, Alex",
 "Icon":2
 }
 """
 Then I receive the status code "200" for the response

#******************DELETE method*************************

@smoke
Scenario: Delete Project By Id
 Given I have a service of "/projects/3662936.json"
 When I send "DELETE" project request to remove a proyect
 Then I receive the status code "200" for the response
