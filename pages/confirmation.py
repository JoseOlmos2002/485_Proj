import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ConfirmationPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session

        # Ensure the frame uses pack layout
        self.pack(fill="both", expand=True)

        # Title
        ttk.Label(self, text="Reservation Confirmation", bootstyle="primary", font=("Helvetica", 18)).pack(pady=20)

        # Output frame
        output_frame = ttk.Frame(self)
        output_frame.pack(padx=20, pady=20)

        # Display reservation details (initially empty, updated later)
        self.confirmation_label = ttk.Label(output_frame, text="", bootstyle="info", justify="left", font=("Helvetica", 12))
        self.confirmation_label.pack(anchor="w")

        # Navigation buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        back_button = ttk.Button(button_frame, text="Back", command=lambda: show_page("MainPage"), bootstyle="secondary")
        back_button.pack(side="left", padx=10)

        exit_button = ttk.Button(button_frame, text="Exit", command=self.quit, bootstyle="danger")
        exit_button.pack(side="left", padx=10)

        # Populate initial data
        self.update_confirmation_display()

    def update_confirmation_display(self):
        # Retrieve data from the session
        name = self.session.get("name", "Not provided")
        email = self.session.get("email", "Not provided")
        current_location = self.session.get("currentlocation", "Not provided")
        destination = self.session.get("destination", "Not provided")
        seat = self.session.get("seat_preference", "Not selected")
        meal_choices = ", ".join(self.session.get("meal_choices", [])) or "None"
        beverage_choices = ", ".join(self.session.get("beverage_choices", [])) or "None"

        # Format the confirmation details
        details = f"""
        Name: {name}
        Email: {email}
        Current Location: {current_location}
        Destination: {destination}
        Seat Preference: {seat}
        Meal Choices: {meal_choices}
        Beverage Choices: {beverage_choices}
        """

        # Update label text
        self.confirmation_label.config(text=details)
