Feature: vehicles entering the car park
    Scenario: A car enters the car park
        Given an empty car park
        When A car with the registration plate "abc" enters the car park
        Then A car with the same reg number should appear in the car parks list of cars 

    Scenario: A duplicate car tries to enter the car park
        Given a carpark that holds a car with the reg number "abc"
        When a second car with the reg number "abc" tries to enter the carpark
        Then only one car with the reg number "abc" should occupy a space in the car park

    Scenario: A car enters the car park then leaves without parking
        Given an empty car park
        When A car with the registration plate "abc" enters the car park and leaves without parking
        Then the car park should be empty


    Scenario Outline: Only cars can enter the car park
        Given an empty car park
        When a <vehicle> tries to enter the car park 
        Then the number of spaces occupied should be <number>

        Examples: Different vehicles
        | vehicle | number |
        | Car | 1 |
        | Lorry | 0 |
        | Tractor | 0 |