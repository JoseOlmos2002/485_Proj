import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import db_connection as db
from datetime import date  

class CheckFlight(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)
        self.show_page = show_page

        parent.pack_propagate(False)  
        self.pack(fill="both", expand=True)

        # Create a frame for the confirmation form
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=20, padx=20, expand=True)

        # Title Label
        ttk.Label(form_frame, text="Flight Confirmation", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))

        # Confirmation number input
        ttk.Label(form_frame, text="Enter confirmation number here:").pack(anchor="w", padx=10, pady=(10, 0))
        self.confirmation_entry = ttk.Entry(form_frame, bootstyle="primary", width=25)
        self.confirmation_entry.pack(pady=(0, 10), padx=10)

        # Submit button
        ttk.Button(form_frame, text="Check Flight", bootstyle="outline-primary", 
                   command=lambda: self.check_flight(show_page, session)).pack(pady=10)
        
        # Submit button
        ttk.Button(form_frame, text="Return to Login", bootstyle="outline-secondary", 
                   command=lambda: self.show_page("LoginPage")).pack(pady=10)

        # Error message label (initially empty)
        self.error_label = ttk.Label(form_frame, text="", bootstyle="danger")
        self.error_label.pack(pady=5)

    def check_flight(self, show_page, session):
        confirmation_number = self.confirmation_entry.get()

        # Retrieve flight details from the database
        flight_info = db.get_flight_info(confirmation_number)

        if flight_info:
            # Manually store each field in the session, and format dates
            session.set("confirmation_number", flight_info['CONFIRMATION_NUMBER'])
            session.set("current_location", flight_info['CURRENT_LOCATION'])
            session.set("destination", flight_info['DESTINATION'])
            
            # Format the date fields into a readable format
            reservation_date = flight_info['RESERVATION_DATE'].strftime("%B %d, %Y")  
            flight_date = flight_info['FLIGHT_DATE'].strftime("%B %d, %Y")  
            
            session.set("reservation_date", reservation_date)
            session.set("flight_date", flight_date)
            
            session.set("name", flight_info['NAME'])
            session.set("seat_preference", flight_info['SEAT_PREFERENCE'])
            session.set("meal_preference", flight_info['MEAL_PREFERENCE'])
            session.set("beverage_choice", flight_info['BEVERAGE_CHOICE'])

            print("Flight information stored in session:", flight_info)
            print(session.get("reservation_date", "blah"))
            print(session.get("flight_date", "blah"))

            
            show_page("FlightDetailsPage")
        else:
            # Display error if flight is not found
            self.error_label.config(text="Flight not found. Please check your confirmation number.")

        # Clear the entry field
        self.confirmation_entry.delete(0, "end")
