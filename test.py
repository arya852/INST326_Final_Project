from ta import TA
import pytest
import re

@pytest.fixture
def ta_instance():
    """ Fixture for creating an instance of the TA class for testing.
    returns
        TA: An instance of the TA class.
    """
    return TA()

def test_display_office_hour_queue(capsys, ta_instance, monkeypatch):
    """ Test the 'display_office_hour_queue' method of the TA class."""
    # mock user input for testing
    monkeypatch.setattr('builtins.input', lambda _: '1')

    # call the function to test
    ta_instance.display_office_hour_queue()

    # capture the output
    captured = capsys.readouterr()

    # Check if the expected output is correct in the captured output
    assert re.search(r"Office Hour Queue:\s*Queue #\s*Name\s*Date", captured.out) is not None

    # close the database connection
    ta_instance.close_connection()


def test_display_daily_questions(capsys, ta_instance, monkeypatch):
    """ Test the 'display_daily_questions' method of the TA class."""
    # mock user input for testing
    monkeypatch.setattr('builtins.input', lambda _: '2')

    # call the function to test
    ta_instance.display_daily_questions()

    # capture the output
    captured = capsys.readouterr()

    # Check if the expected output is correct in the captured output
    assert "Daily Questions:" in captured.out
    assert "Question" in captured.out
    assert "Full Name" in captured.out
    assert "Email Address" in captured.out
    assert "Submission Time" in captured.out

    # close the database connection
    ta_instance.close_connection()


def test_invalid_input(capsys, ta_instance, monkeypatch):
    """ Test for invalid user input in the TA option"""
    # mock invalid user input for testing
    monkeypatch.setattr('builtins.input', lambda _: '3')

    # call the main function
    ta_instance.main()

    # capture the output
    captured = capsys.readouterr()

    # heck if the expected output for invalid input is there
    assert "Invalid input. Please enter a valid option." in captured.out

    # close the database connection
    ta_instance.close_connection()

