import pytest
from simple_interest import *

def test_calculate_simple_interest():
    assert calculate_simple_interest(1000, 5, 2) == 100

def test_main(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3456", "5", "6"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    main()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Interest earned is 1036.80"

# Add more test cases as needed
