Feature: Buy product

    Scenario: Buy a product successfully
        Given I am on the demoblaze homepage

        When I select a product
        And I add the first product to the cart
        And I accept the alert
        And I return to home page
        And I select a second product
        And I add the second product to the cart
        And I accept the alert
        And I go to the cart
        And I place the order with valid information

        Then I should see the confirmation message