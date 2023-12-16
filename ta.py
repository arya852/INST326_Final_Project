from database import DatabaseManager


class TA:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def main(self):
        print("You selected Teaching Assistant.")
        print("What would you like to do?")
        print("1. Assist the students in the Office hour")
        print("2. Answer the daily questions")

        ta_input = input("Enter the number corresponding to your choice: ")

        if ta_input == "1":
            self.display_office_hour_queue()
        elif ta_input == "2":
            self.display_daily_questions()
        else:
            print("Invalid input. Please enter a valid option.")

    def display_office_hour_queue(self):
        self.db_manager.display_office_hour_queue()

    def display_daily_questions(self):
        self.db_manager.display_daily_questions()

    def close_connection(self):
        self.db_manager.close_connection()
