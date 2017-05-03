Feature: Reset

    Scenario: Reset with text
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Pulse button "reset"
        Check if element "text" value is ""

    Scenario: Reset without text
        Given I go to "http://localhost:5000/"
        Pulse button "reset"
        Check if element "text" value is ""

    Scenario: Reset after count
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Pulse button "count"
        Pulse button "reset"
        Check if element "text" value is ""
        Check if result is "('test', 1)"

    Scenario: Reset with text after count
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Pulse button "count"
        Insert text "test2" in element "text"
        Pulse button "reset"
        Check if element "text" value is ""
        Check if result is "('test', 1)"