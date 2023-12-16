import sqlite3
import csv
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_filename='office_hour_queue.db'):
        self.conn = sqlite3.connect(db_filename)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS office_hour_queue (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL,
                    date TEXT NOT NULL,
                    reason TEXT NOT NULL
                )
            ''')

    def insert_record(self, student_name, reason):
        time_now = datetime.now().strftime('%H:%M:%S')
        date_now = datetime.now().strftime('%Y-%m-%d')

        with self.conn:
            self.conn.execute('''
                INSERT INTO office_hour_queue (name, time, date, reason)
                VALUES (?, ?, ?, ?)
            ''', (student_name, time_now, date_now, reason))

    def fetch_records(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM office_hour_queue')
            return cursor.fetchall()

    def close_connection(self):
        self.conn.close()

    def save_to_csv(self, filename):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM office_hour_queue')
            rows = cursor.fetchall()

            with open(filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Check if the file is empty
                if csvfile.tell() == 0:
                    csv_writer.writerow(
                        ['ID', 'Name', 'Time', 'Date', 'Reason'])

                # Get the last ID in the existing CSV
                last_id = 0
                if rows:
                    last_id = rows[-1][0]

                # Fetch and append only the new records
                new_records = self.conn.execute(
                    'SELECT * FROM office_hour_queue WHERE id > ?', (last_id,))

                # Append new records to CSV
                csv_writer.writerows(new_records)

    def save_questions_to_csv(self, question_info, filename='questions.csv'):
        question_data = [
            [question_info.get('question', ''), question_info.get('full_name', ''),
             question_info.get('email_address', ''), datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        ]

        with open(filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if csvfile.tell() == 0:  # Check if file is empty, then write header
                csv_writer.writerow(
                    ['Question', 'Full Name', 'Email Address', 'Submission Time'])
            csv_writer.writerows(question_data)

    def join_queue(self, student_name, reason):
        time_now = datetime.now().strftime('%H:%M:%S')
        date_now = datetime.now().strftime('%Y-%m-%d')

        with self.conn:
            self.conn.execute('''
                INSERT INTO office_hour_queue (name, time, date, reason)
                VALUES (?, ?, ?, ?)
            ''', (student_name, time_now, date_now, reason))

    def display_office_hour_queue(self):
        with open('office_hour_queue.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip header

            print("\nOffice Hour Queue:")
            print("{:<10} {:<20} {:<10}".format("Queue #", "Name", "Date"))
            print("{:<10} {:<20} {:<10}".format("--------", "----", "----"))

            for row in csv_reader:
                queue_number, name, date = row[0], row[1], row[3]
                print("{:<10} {:<20} {:<10}".format(queue_number, name, date))

    def display_queue(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM office_hour_queue')
            rows = cursor.fetchall()

            if not rows:
                print("The queue is currently empty.")
            else:
                print("Current Office Hour Queue:")
                for row in rows:
                    print(
                        f"Queue number: {row[0]}, Name: {row[1]}, Time: {row[2]}, Date: {row[3]}, Reason: {row[4]}")

    def display_daily_questions(self):
        with open('questions.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip header

            print("\nDaily Questions:")
            print("{:<20} {:<20} {:<30} {:<20}".format("Question",
                  "Full Name", "Email Address", "Submission Time"))
            print("{:<20} {:<20} {:<30} {:<20}".format("--------",
                  "---------", "--------------", "---------------"))

            for row in csv_reader:
                question, full_name, email_address, submission_time = row[0], row[1], row[2], row[3]
                print("{:<20} {:<20} {:<30} {:<20}".format(
                    question, full_name, email_address, submission_time))

    def close_connection(self):
        self.conn.close()
