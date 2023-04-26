# Created by user at 4/25/23
Feature: Main Page Tests


  Scenario: Verify Price filter functionality
    Given Open Cureskin page
    When Close popup
    When Click on Shop All section
    And Adjust the price filter so change in number of product
    Then Verify number of product changes
    And Verify product displayed are within the price filter