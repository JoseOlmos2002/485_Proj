import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk  

class Congratulations(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page

        # Prevent parent from resizing and make it fill the window
        parent.pack_propagate(False)
        self.pack(fill="both", expand=True)

        # Create a container frame to hold both the image and content
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Load and display an image on the left side
        image = Image.open("pages/images/Flight_Attendant.jpg")  
        image = image.resize((400, 600)) 
        photo = ImageTk.PhotoImage(image)

        image_label = ttk.Label(container, image=photo)
        image_label.image = photo  
        image_label.pack(side="left", padx=20, pady=20)  

        # Create a frame for the content (shifted to the right)
        content_frame = ttk.Frame(container)
        content_frame.pack(side="right", padx=50, pady=20)

     
        ttk.Label(
            content_frame,
            text="🎉 Congratulations! Your Reservation is Confirmed 🎉",
            bootstyle="success",
            wraplength=250,
            font=("Helvetica", 18, "bold")  # Smaller font size
        ).pack(pady=20)

        # Output frame (holds confirmation details)
        output_frame = ttk.Frame(content_frame)
        output_frame.pack(padx=20, pady=20)


        # Information label with wraplength
        self.information_label = ttk.Label(
            output_frame,
            text="Please take note of the following confirmation number. You can access the created flight info with this number.",
            justify="center",
            wraplength=200,  # Ensures text wraps if it's too long
            font=("Helvetica", 12),  # Smaller font size
            foreground="black"
        )
        self.information_label.pack(pady=10)

        # Confirmation text with wraplength
        self.confirmation_text = ttk.Label(
            output_frame,
            text="Confirmation Number:",
            justify="center",  # Center the text horizontally
            font=("Helvetica", 20, "bold"),  # Smaller font size
            foreground="black",
            wraplength=400  # Specify wrap length in pixels
        )
        self.confirmation_text.pack(pady=10)

        # Confirmation number (dynamic)
        self.confirmation_number_label = ttk.Label(
            output_frame,
            text="",
            bootstyle="info",
            justify="center",
            font=("Helvetica", 25, "bold"),
            foreground="black",
            wraplength=400  # Wraps text after this width
        )
        self.confirmation_number_label.pack(pady=10)


        self.extra_label = ttk.Label(
            output_frame,
            text="Details of reserved flight:",
            justify="center",
            wraplength=200,  # Ensures text wraps if it's too long
            font=("Helvetica", 18),  # Smaller font size
            foreground="black"
        )
        self.extra_label.pack(pady=10)

        # Reservation details (initially empty, updated later)
        self.confirmation_label = ttk.Label(
            output_frame,
            text="",
            justify="left",
            font=("Helvetica", 14),  # Smaller font size
            wraplength=400  # Keeps long text within bounds
        )
        self.confirmation_label.pack(pady=5)

        # Navigation buttons
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(pady=20)

        logout_button = ttk.Button(
            button_frame,
            text="Logout",
            command=self.logout,
            bootstyle="outline-danger"
        )
        logout_button.pack()

        # Populate initial data
        self.update_congratulations_display()

    def update_congratulations_display(self):
        # Retrieve data from the session
        name = self.session.get("name", "Not provided")
        email = self.session.get("email", "Not provided")
        current_location = self.session.get("currentlocation", "Not provided")
        destination = self.session.get("destination", "Not provided")
        seat = self.session.get("seat_preference", "Not selected")
        meal_choices = self.session.get("meal_choices", "Not selected")
        beverage_choices = self.session.get("beverage_choices", "Not selected")

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

        # Update confirmation number with hashtag
        confirmation_number = self.session.get("confirmation_number", "Not provided")
        confirmation_number = f"#{confirmation_number}" if confirmation_number != "Not provided" else confirmation_number
        self.confirmation_number_label.config(text=confirmation_number)

    def logout(self):
        # Clear session data and return to the login page
        self.session.clear()
        self.show_page("LoginPage")
