import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LocationSelectionPage(ttk.Frame):
    def __init__(self, parent, show_page):
        super().__init__(parent)
        
        # Sample locations for the choice boxes
        self.locations = ["New York", "Los Angeles", "Chicago", "Miami", "Dallas"]

        # Create a frame to hold all widgets
        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(padx=20, pady=20, expand=True)

        # Current Location
        ttk.Label(self.container_frame, text="Current Location:", font=("Helvetica", 12)).pack(pady=10)
        self.current_location_var = ttk.StringVar()
        self.current_location_menu = ttk.Combobox(self.container_frame, textvariable=self.current_location_var, values=self.locations, state="readonly", bootstyle="primary")
        self.current_location_menu.pack(pady=5)

        # Destination Location
        ttk.Label(self.container_frame, text="Destination:", font=("Helvetica", 12)).pack(pady=10)
        self.destination_var = ttk.StringVar()
        self.destination_menu = ttk.Combobox(self.container_frame, textvariable=self.destination_var, values=self.locations, state="readonly", bootstyle="primary")
        self.destination_menu.pack(pady=5)

        # Submit button
        self.submit_button = ttk.Button(self.container_frame, text="Submit", bootstyle=SUCCESS, command=self.submit_data)
        self.submit_button.pack(pady=20)

        # Result label
        self.result_label = ttk.Label(self.container_frame, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # Navigation buttons
        ttk.Button(self.container_frame, text="Next Page", bootstyle=PRIMARY, command=lambda: show_page("MainPage")).pack(pady=10)

    def submit_data(self):
        # Get selected current location and destination
        current_location = self.current_location_var.get()
        destination = self.destination_var.get()

        # Update result label with the selected data
        if current_location and destination:
            result = f"Current Location: {current_location}\nDestination: {destination}"
        else:
            result = "Please select both locations!"
        
        # Show result in label
        self.result_label.config(text=result)
