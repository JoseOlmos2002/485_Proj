import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import db_connection as db
from PIL import Image, ImageTk 

class LoginPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        
        parent.pack_propagate(False)
        self.pack(fill="both", expand=True)

        # Create a container frame to hold both the image and form
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Load and display an image on the left side
        image = Image.open("pages/images/Plane.jpg") 
        image = image.resize((400, 650))  # Resize as needed
        photo = ImageTk.PhotoImage(image)

        image_label = ttk.Label(container, image=photo)
        image_label.image = photo 
        image_label.pack(side="left", padx=20, pady=20)  

        # Create a frame for the login form (shifted to the right)
        form_frame = ttk.Frame(container)
        form_frame.pack(side="right", padx=50, pady=20, anchor="e")

        # Title Labels
        ttk.Label(form_frame, text="WELCOME TO FLIGHT RESERVATION", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(form_frame, text="Please login below", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))

        # Username Entry
        ttk.Label(form_frame, text="Username:").pack(anchor="w", padx=10, pady=(10, 0))
        self.username_entry = ttk.Entry(form_frame, bootstyle="primary", width=25)
        self.username_entry.pack(pady=(0, 10), padx=10)

        # Password Entry
        ttk.Label(form_frame, text="Password:").pack(anchor="w", padx=10, pady=5)
        self.password_entry = ttk.Entry(form_frame, bootstyle="primary", width=25, show="*")
        self.password_entry.pack(pady=(0, 10), padx=10)

        # Buttons with rounded corners and smoother look
        ttk.Button(form_frame, text="Login", bootstyle="outline-primary", command=lambda: self.login(show_page, session)).pack(pady=10, padx=10)
        ttk.Button(form_frame, text="Sign Up", bootstyle="outline-secondary", command=lambda: show_page("SignupPage")).pack(pady=10, padx=10)
        ttk.Button(form_frame, text="Check Existing Flight", bootstyle="outline-info", command=lambda: show_page("CheckFlight")).pack(pady=10, padx=10)

    def login(self, show_page, session):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if db.logging_in(username, password):
            print("Matching user found in Database. Logging in.")
            session.set("username", username)
            show_page("LocationSelectionPage")
        else:
            error_label = ttk.Label(self, text="Invalid email or password. Please try again.", bootstyle="danger")
            error_label.pack(pady=5)

        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
