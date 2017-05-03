Feature: Count
    
    Scenario: count
        Given I go to "http://localhost:5000/"
        Insert text "test test2 test2" in element "text"
        Pulse button "count"
        Check if element "text" value is ""
        Check if result is "('test2', 2)('test', 1)"

    Scenario: count after count
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Pulse button "count"
        Check if element "text" value is ""
        Check if result is "('test', 1)"
        Insert text "test2" in element "text"
        Pulse button "count"
        Check if element "text" value is ""
        Check if result is "('test2', 1)"

    Scenario: count without text
        Given I go to "http://localhost:5000/"
        Pulse button "count"
        Check if element "text" value is ""
        Check if result is ""

    Scenario: count without text after count
        Given I go to "http://localhost:5000/"
        Insert text "test" in element "text"
        Pulse button "count"
        Check if element "text" value is ""
        Check if result is "('test', 1)"
        Pulse button "count"
        Check if element "text" value is ""
        CCheck if result is "('test', 1)"