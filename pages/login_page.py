import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LoginPage(ttk.Frame):
    def __init__(self, parent, show_page):
        super().__init__(parent)

        # Make the parent frame expand and fill the window
        parent.pack_propagate(False)  # Prevent the parent from resizing with the frame
        self.pack(fill="both", expand=True)

        # Create a frame for the login form (this will be centered)
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=20, padx=20, expand=True)

        # Create a label for the title
        ttk.Label(form_frame, text="WELCOME TO FLIGHT RESERVATION", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(form_frame, text="", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(form_frame, text="Login", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))

        # Create the form contents inside form_frame
        ttk.Label(form_frame, text="Email:").pack(anchor="w", padx=10, pady=(10, 0))
        self.email_entry = ttk.Entry(form_frame, bootstyle="primary", width=25)
        self.email_entry.pack(pady=(0, 10), padx=10)

        ttk.Label(form_frame, text="Password:").pack(anchor="w", padx=10, pady=5)
        self.password_entry = ttk.Entry(form_frame, bootstyle="primary", width=25, show="*")  # Hide password text
        self.password_entry.pack(pady=(0, 10), padx=10)

        # Create the login button inside form_frame
        ttk.Button(form_frame, text="Login", bootstyle=PRIMARY, command=lambda: self.login(show_page)).pack(pady=10)
        ttk.Button(form_frame, text="Sign Up", bootstyle=SECONDARY, command=lambda: show_page("SignupPage")).pack(pady=10)

    def login(self, show_page):
        # Hardcoded credentials for login validation
        correct_email = "user@example.com"
        correct_password = "password123"
        
        # Get user input
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Validate the credentials
        if email == correct_email and password == correct_password:
            show_page("LocationSelectionPage")  # Switch to the next page (MainPage)
        else:
            error_label = ttk.Label(self, text="Invalid email or password. Please try again.", bootstyle="danger")
            error_label.pack(pady=5)
