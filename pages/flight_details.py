import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import db_connection as db
from PIL import Image, ImageTk  

class FlightDetailsPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page

        # Create a container to hold both the image and details section
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Load and display an image on the left side
        image = Image.open("pages/images/Plane_Ticket.jpg")  
        image = image.resize((400, 575))  # Resize as needed
        photo = ImageTk.PhotoImage(image)

        image_label = ttk.Label(container, image=photo)
        image_label.image = photo 
        image_label.pack(side="left", padx=20, pady=20)  

        # Create a frame for the flight details section (shifted to the right)
        details_frame = ttk.Frame(container)
        details_frame.pack(side="right", padx=50, pady=20, anchor="e")

        # Title (without background color)
        title_label = ttk.Label(details_frame, text="Flight Details for:", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=(10, 20))

        self.confirmation_label = ttk.Label(details_frame, text="", font=("Helvetica", 16, "bold"))
        self.confirmation_label.pack(pady=(5, 5))

        # Output frame with a styled border
        output_frame = ttk.Labelframe(details_frame, text="Your Reservation Details", bootstyle="info", padding=15)
        output_frame.pack(fill="both", expand=True, padx=15, pady=10)

        # Display flight details
        self.details_label = ttk.Label(
            output_frame, text="", wraplength=350, justify="left", anchor="w"  # Increased wraplength
        )

        self.details_label.pack(fill="x", padx=15, pady=10)  # Allow more space

        # Navigation buttons (stacked)
        button_frame = ttk.Frame(details_frame)
        button_frame.pack(pady=20)

        back_button = ttk.Button(
            button_frame, text="Back", command=lambda: show_page("CheckFlight"),
            bootstyle="secondary-outline"
        )
        back_button.pack(padx=15, pady=5, anchor="center")  # Auto-size based on text

        exit_button = ttk.Button(
            button_frame, text="Return to Login Page", command=self.return_to_login,
            bootstyle="danger-outline"
        )
        exit_button.pack(padx=15, pady=5, anchor="center")  # Auto-size based on text

        # Populate initial data
        self.update_flight_details()

    def update_flight_details(self):
        # Retrieve data from the session
        details = {
            "Name": self.session.get("name", "Not provided"),
            "Current Location": self.session.get("current_location", "Not provided"),
            "Destination": self.session.get("destination", "Not provided"),
            "Reserved On": self.session.get("reservation_date", "Not provided"),
            "Flight Date": self.session.get("flight_date", "Not provided"),
            "Meal Choice": self.session.get("meal_preference", "Not provided"),
            "Beverage Choice": self.session.get("beverage_choice", "Not assigned"),
            "Assigned Seat": self.session.get("seat_preference", "Not selected"),
        }

        # Format details for display
        formatted_details = "\n".join([f"• {key}: {value}" for key, value in details.items()])
        self.details_label.config(text=formatted_details)

        #Adding confirmation number:
        confirmation_number = self.session.get("confirmation_number", "Not provided")
        self.confirmation_label.config(text = f"#{confirmation_number}")

    def return_to_login(self):
        self.session.clear()
        self.show_page("LoginPage")
