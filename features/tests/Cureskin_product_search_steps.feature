# Created by user at 4/20/23
Feature: Cureskin Product Search


  Scenario: User can shop by product Sunscreens
    Given Open Cureskin page
    When Click on "Shop by product"
    When Select sunscreens
    Then Verify the first product in Sunscreen


  Scenario: User can search for a product that doesn't exist
    #Given Open Cureskin page
    #When Click on search button
    #And Enter a product name Vitamin D Cream that does not exist to search box
    #Then Verify no results returned on the drop-down
    #And Click on search button on the drop-down
    #Then Verify No results found  message is shown