import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SignupPage(ttk.Frame):
    def __init__(self, parent, show_page):
        super().__init__(parent)

        # Make the parent frame expand and fill the window
        parent.pack_propagate(False)  # Prevent the parent from resizing with the frame
        self.pack(fill="both", expand=True)

        # Create a frame for the signup form (this will be centered)
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=20, padx=20, expand=True)

        # Create a label for the title
        ttk.Label(form_frame, text="WELCOME TO FLIGHT RESERVATION", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(form_frame, text="", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))
        ttk.Label(form_frame, text="Sign Up", font=("Helvetica", 16, "bold")).pack(pady=(0, 10))

        # Create the form contents inside form_frame
        ttk.Label(form_frame, text="Email:").pack(anchor="w", padx=10, pady=(10, 0))
        self.email_entry = ttk.Entry(form_frame, bootstyle="primary", width=25)
        self.email_entry.pack(pady=(0, 10), padx=10)

        ttk.Label(form_frame, text="Username:").pack(anchor="w", padx=10, pady=5)
        self.username_entry = ttk.Entry(form_frame, bootstyle="primary", width=25)
        self.username_entry.pack(pady=(0, 10), padx=10)

        ttk.Label(form_frame, text="Password:").pack(anchor="w", padx=10, pady=5)
        self.password_entry = ttk.Entry(form_frame, bootstyle="primary", width=25, show="*")  # Hide password text
        self.password_entry.pack(pady=(0, 10), padx=10)

        ttk.Label(form_frame, text="Confirm Password:").pack(anchor="w", padx=10, pady=5)
        self.confirm_password_entry = ttk.Entry(form_frame, bootstyle="primary", width=25, show="*")  # Hide password text
        self.confirm_password_entry.pack(pady=(0, 10), padx=10)

        # Create the sign-up button inside form_frame
        ttk.Button(form_frame, text="Sign Up", bootstyle=PRIMARY, command=lambda: self.signup(show_page)).pack(pady=10)
        ttk.Button(form_frame, text="Return to Login", bootstyle=PRIMARY, command=lambda: show_page("LoginPage")).pack(pady=10)
 
    def signup(self, show_page):
        # Get user input
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Basic validation
        if not email or not username or not password or not confirm_password:
            error_label = ttk.Label(self, text="All fields are required. Please fill in all details.", bootstyle="danger")
            error_label.pack(pady=5)
            return

        if password != confirm_password:
            error_label = ttk.Label(self, text="Passwords do not match. Please try again.", bootstyle="danger")
            error_label.pack(pady=5)
            return

        # If everything is valid, proceed (you can add more logic to save the user data, etc.)
        success_message = f"Sign Up Successful!\nEmail: {email}\nUsername: {username}"
        success_label = ttk.Label(self, text=success_message, bootstyle="success")
        success_label.pack(pady=5)

        # Optionally, navigate to the next page after sign-up
        # show_page("LocationSelectionPage")  # Switch to another page after successful sign-up
