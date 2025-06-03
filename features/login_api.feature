Feature: User Authentication
  As a user
  I want to sign up and log in to the system
  So that I can access protected features

  Scenario: Sign up a new user successfully
    Given I have a unique valid username and password
    When I send a signup request
    Then I should receive a success message or user already exists

  Scenario: Sign up with an existing user
    Given I have already registered the same user
    When I try to sign up again
    Then I should receive an error message

  Scenario: Log in with valid credentials
    Given I am a registered user
    When I send a login request with correct credentials
    Then I should receive a token or success message

  Scenario: Log in with invalid credentials
    Given I am not a registered user
    When I send a login request with incorrect credentials
    Then I should receive an error message