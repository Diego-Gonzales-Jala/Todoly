# Created by Alex Garcia at 11/23/2017
@projectsFeature
Feature: Projects
As ToDo user
 I want to manage my projects
 Because Project holds a number of items. Every Item in the system belongs to a Project.
 If an Item doesn’t have a Project assigned to it, it only displayed in the Inbox.
 Projects can be in hierarchy containing other projects.

Background: User authenticated
    Given I have a new user authenticated
@CRUD
Scenario: Create New Project [CRUD]
 Given I have a service of "/projects.json"
 When I send "POST" project request with generic body.json:
 """
 {
  "Content": "My New GenericProject-ALEX",
  "Icon": 4
  }
 """
 Then A new project should be insert in the database


@CRUD
Scenario: Update Project By Id [CRUD]
 Given I have a service of "/projects/3663174.json"
 When I send "PUT" project request with generic body.json to update a proyect:
 """
 {
 "Content": "My Update GenericProject-Alex05, Alex",
 "Icon":2
 }
 """
Then The project should be updated in the database


@CRUD
Scenario: Delete Project By Id [CRUD]
 Given I have a service of "/projects/3663181.json"
 When I send "DELETE" project request to remove a proyect
 Then The project should be deleted in the database