import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class LocationSelectionPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page

        # Sample locations for the choice boxes
        self.locations = [
        "New York", "Los Angeles", "Chicago", "Miami", "Dallas",
        "London", "Paris", "Tokyo", "Berlin", "Sydney",
        "Rome", "Barcelona", "Dubai", "Toronto", "Singapore",
        "Hong Kong", "Amsterdam", "San Francisco", "Seoul", "Toronto",
        "Mexico City", "Bangkok", "Moscow", "Rio de Janeiro", "Cape Town"
        ]

        self.locations.sort()

        # Create a frame to hold all widgets
        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(padx=20, pady=20, expand=True)

        # Intro: show username
        self.username_label = ttk.Label(self.container_frame, text=f"Username: {self.session.get('username', 'Guest')}",font=("Helvetica", 16, "bold"))
        self.username_label.pack(pady=10, padx=10)

        #Instructions:
        self.instructions = ttk.Label(self.container_frame, text="Please choose your location and desired destination:",font=("Helvetica", 16, "bold"))
        self.instructions.pack(pady=10, padx=10)

        # Current Location
        ttk.Label(self.container_frame, text="Current Location:", font=("Helvetica", 14)).pack(pady=10)
        self.current_location_var = ttk.StringVar()
        self.current_location_menu = ttk.Combobox(self.container_frame, textvariable=self.current_location_var, values=self.locations, state="readonly", bootstyle="primary")
        self.current_location_menu.pack(pady=5)

        # Destination Location
        ttk.Label(self.container_frame, text="Destination:", font=("Helvetica", 14)).pack(pady=10)
        self.destination_var = ttk.StringVar()
        self.destination_menu = ttk.Combobox(self.container_frame, textvariable=self.destination_var, values=self.locations, state="readonly", bootstyle="primary")
        self.destination_menu.pack(pady=5)

        # Navigation buttons
        ttk.Button(self.container_frame, text="Next Page", bootstyle="outline-primary", command=self.submit_data).pack(pady=10)

    def submit_data(self):
        # Get selected current location and destination
        current_location = self.current_location_var.get()
        destination = self.destination_var.get()

        # Validate and store data
        if current_location and destination:
            self.session.set('currentlocation', current_location)
            self.session.set('destination', destination)
            self.show_page("MainPage")  # Navigate to MainPage
        else:
            messagebox.showwarning("Input Error", "Please select both locations!")

    def update_username_display(self):
        # This function can be called after updating the session username
        self.username_label.config(text=f"Welcome, {self.session.get('username', 'Guest')}.")
