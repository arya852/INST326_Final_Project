from database import DatabaseManager
from schedule import Schedule


class Student:
    """ Class representing a Student in the INST326 Office Hour System.

    Attributes:
        db_manager (DatabaseManager): Instance of the DatabaseManager for database operations.
        schedule (Schedule): Instance of the Schedule for managing office hour schedules.
    """
    
    def __init__(self):
        """ Student instance with a DatabaseManager and a Schedule."""
        self.db_manager = DatabaseManager()
        self.schedule = Schedule()

    def main(self):
        """ Main function for Student-specific actions.

        Returns:
            dict or None: If the student submits a question, returns the question information. Otherwise, returns None.
        """

        print("You selected Student.")
        print("What would you like to do?")
        print("1. Join the office hour queue")
        print("2. Office hour schedule")
        print("3. Leave a question for TA to respond by the end of the day")

        student_input = input(
            "Enter the number corresponding to your choice: ")

        if student_input == "1":
            self.join_office_hour_queue()
        elif student_input == "2":
            print()
            print("Here is the office hour schedule:")
            self.schedule.display_schedule()
            print()
        elif student_input == "3":
            print()
            question = input("Write your question: ")
            full_name = input("Enter your full name: ")
            email_address = input("Enter your UMD email address: ")

            question_info = {
                'question': question,
                'full_name': full_name,
                'email_address': email_address
            }
            self.db_manager.save_questions_to_csv(question_info)
            print()
            print(
                "Your question has been submitted. TA will respond by the end of the day.")
            return question_info
        else:
            print("Invalid input. Please enter a valid option.")

    def join_office_hour_queue(self):
        """ Allows the student to join the office hour queue."""

        print()
        print("You joined the office hour queue.")
        print()
        student_name = input("Enter your full name: ")
        reason = input("Enter the reason (assignments or module question): ")
        print()
        self.db_manager.join_queue(student_name, reason)
        self.db_manager.display_queue()
        self.db_manager.save_to_csv('office_hour_queue.csv')

    def close_connection(self):
        """ Closes the database connection."""
        self.db_manager.close_connection()
