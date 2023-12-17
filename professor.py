from database import DatabaseManager
from schedule import Schedule
import csv
import re


class Professor:
    """ Class representing a Professor in the INST326 Office Hour System.

    Attributes:
        db_manager (DatabaseManager): Instance of the DatabaseManager for database operations.
        schedule (Schedule): Instance of the Schedule for managing office hour schedules.
    
    """
    def __init__(self):
        """ Initializes a Professor instance with a DatabaseManager and a Schedule."""
        self.db_manager = DatabaseManager()
        self.schedule = Schedule()

    def main(self):
        """ Main function for keeping Professor-specific actions."""

        print()
        print("You selected Professor.")
        print("What would you like to do?")
        print()
        print("1. View Office Hour Schedule")
        print("2. Access Attendance")
        print()
        professor_input = input(
            "Enter the number corresponding to your choice: ")

        if professor_input == "1":
            self.schedule.display_schedule()
            print()
        elif professor_input == "2":
            print()
            print("How would you like to access attendance?")
            print("1. By Date")
            print("2. By Reason")
            attendance_option = input(
                "Enter the number corresponding to your choice: ")

            if attendance_option == "1":
                print()
                date = input("Enter the date (YYYY-MM-DD): ")
                print()
                self.display_attendance_by_date(date)
                print()
            elif attendance_option == "2":
                print()
                reason = input("Enter the reason: ")
                print()
                self.display_attendance_by_reason(reason)
            else:
                print("Invalid input. Please enter a valid option.")
        else:
            print("Invalid input. Please enter a valid option.")

    def display_attendance_by_date(self, date):
        """ Displays attendance information for a specific date.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.
        """

        try:
            with open('office_hour_queue.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header

                date_pattern = re.compile(f'^{date}')
                rows = [
                    row for row in csv_reader if date_pattern.match(row[3])]

                if not rows:
                    print(f"No attendance information available for {date}.")
                else:
                    print(f"Attendance on {date}:")
                    for row in rows:
                        print(
                            f"Queue number: {row[0]}, Name: {row[1]}, Time: {row[2]}, Reason: {row[4]}")
        except FileNotFoundError:
            print("Attendance file not found.")

    def display_attendance_by_reason(self, reason):
        """ Displays attendance information for a specific reason.

        Args:
            reason (str): The reason for attendance.
        """
        try:
            with open('office_hour_queue.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header

                reason_pattern = re.compile(f'.*{reason}.*', re.IGNORECASE)
                rows = [
                    row for row in csv_reader if reason_pattern.search(row[4])]

                if not rows:
                    print(
                        f"No attendance information available for the reason: {reason}.")
                else:
                    print(f"Attendance for the reason: {reason}")
                    for row in rows:
                        print(
                            f"Queue number: {row[0]}, Name: {row[1]}, Time: {row[2]}, Date: {row[3]}")
        except FileNotFoundError:
            print("Attendance file not found.")

    def close_connection(self):
        """ Close the database connection. """
        self.db_manager.close_connection()
