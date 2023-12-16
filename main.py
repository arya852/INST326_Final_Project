from student import Student
from ta import TA
from professor import Professor


def get_user():
    print("\nWelcome to the INST326 Office Hour System!")
    print("\nPlease select the respective number if you are a:")
    print("1. Professor")
    print("2. Teaching Assistant")
    print("3. Student")

    user_input = input("\nEnter the number corresponding to your role: ")

    if user_input == "1":
        return Professor()
    elif user_input == "2":
        return TA()
    elif user_input == "3":
        return Student()
    else:
        print("Invalid input. Please enter a valid option.")


if __name__ == "__main__":
    user_app = get_user()
    if user_app:
        user_app.main()
        user_app.close_connection()
    else:
        print("Invalid user role.")
