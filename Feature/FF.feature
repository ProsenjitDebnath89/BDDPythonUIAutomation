# Created by prodebna at 9/2/2020
Feature: Feature File Demo for Selenium with Python BDD Framework
  # Enter feature description here
  @tag1
  Scenario Outline: TC003_Validate_Flipkart_Login
    Given Open Browser and launch application "<TestcaseName>"
    When Provide credential UserID and Password
    Then Validate whether Login is successful or not
    Then Logout
    Examples:
      |TestcaseName|
      |TC003_Validate_Flipkart_Login|
