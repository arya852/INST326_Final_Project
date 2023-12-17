from database import DatabaseManager

class TA:
    """ Class representing a Teaching Assistant (TA) in the INST326 Office Hour System.

    Attributes:
        db_manager (DatabaseManager): Instance of the DatabaseManager for database operations.
    """
    
    def __init__(self):
        """ Initializes a TA instance with a DatabaseManager."""
        self.db_manager = DatabaseManager()

    def main(self):
        """ Main function for TA-specific actions."""

        print()
        print("You selected Teaching Assistant.")
        print()
        print("What would you like to do?")
        print("1. Assist the students in the Office hour")
        print("2. Answer the daily questions")
        print()
        ta_input = input("Enter the number corresponding to your choice: ")

        if ta_input == "1":
            self.display_office_hour_queue()
        elif ta_input == "2":
            self.display_daily_questions()
            print()
        else:
            print("Invalid input. Please enter a valid option.")

    def display_office_hour_queue(self):
        """ Displays the current office hour queue."""
        self.db_manager.display_office_hour_queue()

    def display_daily_questions(self):
        """ Displays the daily questions submitted by students."""
        self.db_manager.display_daily_questions()

    def close_connection(self):
        """ Closes the database connection."""
        self.db_manager.close_connection()
