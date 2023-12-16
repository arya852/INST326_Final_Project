class Schedule:
    def display_schedule(self):
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
