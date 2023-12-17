class Schedule:
    """ Class representing the office hour schedule for the INST326 Office Hour System."""

    def display_schedule(self):
        """ Displays the office hour schedule for each day.

        The schedule is hardcoded for demonstration purposes. In future, it could be fetched data from the
        a database or another external API source.

        The displayed schedule includes the day, and for each day, the names of TAs along with
        their corresponding office hours. """

        print("\nOffice Hour Schedule:")
        print("\n{:<15} {:<25}".format("Day", "Office Hours"))
        print("{:<15} {:<25}".format("--------------", "-------------------"))

        schedule = {
            "Monday": [("Deepak", "7 AM - 9 AM"), ("Sana", "11 AM - 2 PM")],
            "Tuesday": [("Ben", "1 PM - 3 PM")],
            "Wednesday": [("Deepak", "7 AM - 9 AM"), ("Sana", "11 AM - 2 PM"), ("Danny", "2 PM - 4 PM")],
            "Thursday": [],
            "Friday": [("Manuel", "8 AM - 10 AM"), ("Sana", "12 PM - 2 PM"), ("Danny", "2 PM - 4 PM")],
        }

        for day, slots in schedule.items():
            office_hours = [f"{name} ({time})" for name, time in slots]
            print("{:<15} {:<25}".format(day, ", ".join(office_hours)))
