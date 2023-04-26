# Created by user at 4/20/23
Feature: Cureskin Add to Cart Test


  Scenario: User can delete an item from the cart
    Given Open Cureskin page
    When Close popup
    And Click on search button
    When Enter a product name Hydration Gel
    And Click on product
    And Click add to cart
    When Verify Hydration Gel in cart
    And Delete product from cart
    Then Verify cart is empty



