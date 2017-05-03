Feature: Insert text

    Scenario: Insert text
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Check if element "text" value is "test"

    Scenario: Insert 101 characters text
        Given I go to "http://localhost:5000/"
        Insert text "testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttO" in element "text"
        Check if element "text" value is "testtttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"
        

