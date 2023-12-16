from database import DatabaseManager
from schedule import Schedule


class Student:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.schedule = Schedule()

    def main(self):
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
            print("Here is the office hour schedule:")
            self.schedule.display_schedule()
        elif student_input == "3":
            question = input("Write your question: ")
            full_name = input("Enter your full name: ")
            email_address = input("Enter your UMD email address: ")

            question_info = {
                'question': question,
                'full_name': full_name,
                'email_address': email_address
            }
            self.db_manager.save_questions_to_csv(question_info)

            print(
                "Your question has been submitted. TA will respond by the end of the day.")
            return question_info
        else:
            print("Invalid input. Please enter a valid option.")

    def join_office_hour_queue(self):
        print("You joined the office hour queue.")
        student_name = input("Enter your full name: ")
        reason = input("Enter the reason (assignments or module question): ")

        self.db_manager.join_queue(student_name, reason)
        self.db_manager.display_queue()
        self.db_manager.save_to_csv('office_hour_queue.csv')

    def close_connection(self):
        self.db_manager.close_connection()
