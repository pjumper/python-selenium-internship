# Created by user at 4/20/23
Feature: Cureskin Product Search


  Scenario: User can shop by product Sunscreens
    Given Open Cureskin page
    When Click on "Shop by product"
    And Select sunscreens
    Then Verify the first product in Sunscreen

