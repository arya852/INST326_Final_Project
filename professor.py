from database import DatabaseManager
from schedule import Schedule
import csv
import re


class Professor:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.schedule = Schedule()

    def main(self):
        print("You selected Professor.")
        print("What would you like to do?")
        print("1. View Office Hour Schedule")
        print("2. Access Attendance")

        professor_input = input(
            "Enter the number corresponding to your choice: ")

        if professor_input == "1":
            self.schedule.display_schedule()
        elif professor_input == "2":
            print("How would you like to access attendance?")
            print("1. By Date")
            print("2. By Reason")
            attendance_option = input(
                "Enter the number corresponding to your choice: ")

            if attendance_option == "1":
                date = input("Enter the date (YYYY-MM-DD): ")
                self.display_attendance_by_date(date)
            elif attendance_option == "2":
                reason = input("Enter the reason: ")
                self.display_attendance_by_reason(reason)
            else:
                print("Invalid input. Please enter a valid option.")
        else:
            print("Invalid input. Please enter a valid option.")

    def display_attendance_by_date(self, date):
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
        self.db_manager.close_connection()
