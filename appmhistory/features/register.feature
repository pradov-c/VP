Feature: Register Patient
 Scenario: Register new Patient
    Given service is up
    When I make a Post request to register a Patient with "345", "Maria Robles" and "2017-01-12"
    Then HTTP 201 is returned


