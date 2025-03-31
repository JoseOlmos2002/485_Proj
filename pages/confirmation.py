import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import db_connection as db

class ConfirmationPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page


        self.pack(fill="both", expand=True)


        container = ttk.Frame(self)
        container.pack(expand=True, fill="both")


        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # Main frame (holds everything)
        main_frame = ttk.Frame(container)
        main_frame.grid(row=0, column=0)

        # Title
        ttk.Label(
            main_frame, 
            text="Reservation Confirmation", 
            font=("Helvetica", 20, "bold"),
            anchor="center"
        ).pack(pady=20)

        ttk.Label(
            main_frame, 
            text="Please ensure all information is correct. You may update any information by returning to the previous page.", 
            font=("Helvetica", 18),
            anchor="center",
            justify = "center",
            wraplength=400
        ).pack(pady=20)

   
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(pady=20)

        # Display reservation details (initially empty, updated later)
        self.confirmation_label = ttk.Label(
            output_frame, 
            text="", 
            font=("Helvetica", 16),
            anchor="center"
        )
        self.confirmation_label.pack(anchor="center", fill="x")

    
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        confirm_button = ttk.Button(
            button_frame, 
            text="Confirm Flight", 
            command=self.confirm_flight, 
            bootstyle="outline-success"
        )
        confirm_button.pack(pady=10) 

        back_button = ttk.Button(
            button_frame, 
            text="Back", 
            command=lambda: show_page("MainPage"), 
            bootstyle="outline-danger"
        )
        back_button.pack(pady=10)  


        # Populate initial data
        self.update_confirmation_display()

    def update_confirmation_display(self):
        name = self.session.get("name", "Not provided")
        email = self.session.get("email", "Not provided")
        current_location = self.session.get("currentlocation", "Not provided")
        destination = self.session.get("destination", "Not provided")
        seat = self.session.get("seat_preference", "Not selected")
        meal_choices = self.session.get("meal_choices", "Not selected")
        beverage_choices = self.session.get("beverage_choices", "Not selected")

        details = f"""
        Name: {name}
        Email: {email}
        Current Location: {current_location}
        Destination: {destination}
        Seat Preference: {seat}
        Meal Choice: {meal_choices}
        Beverage Choice: {beverage_choices}
        """

        self.confirmation_label.config(text=details)

    def confirm_flight(self):
        name = self.session.get("name", "Not provided")
        current_location = self.session.get("currentlocation", "Not provided")
        destination = self.session.get("destination", "Not provided")
        seat = self.session.get("seat_preference", "Not selected")
        meal_choices = self.session.get("meal_choices", "Not selected")
        beverage_choices = self.session.get("beverage_choices", "Not selected")

        confirmation_number = db.generate_confirmation_number()
        self.session.set("confirmation_number", confirmation_number)

        db.add_reservation(current_location, destination, name, seat, meal_choices, beverage_choices, confirmation_number)

        self.show_page("Congratulations")
