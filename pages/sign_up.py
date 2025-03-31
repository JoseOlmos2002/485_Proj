import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from . import db_connection as db

class SignupPage(ttk.Frame):
    def __init__(self, parent, show_page):
        super().__init__(parent)

        
        parent.pack_propagate(False)  
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
        ttk.Button(form_frame, text="Sign Up", bootstyle="outline-primary", command=lambda: self.signup(show_page)).pack(pady=10)
        ttk.Button(form_frame, text="Return to Login", bootstyle="outline-secondary", command=lambda: show_page("LoginPage")).pack(pady=10)

    def is_valid_email(self, email):
        """Checks if the email is in a valid format."""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)
    
    def clear_fields(self):
        """Clears all input fields after signup."""
        self.email_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_password_entry.delete(0, "end")

    def signup(self, show_page):
        # Get user input
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Basic validation
        if not email or not username or not password or not confirm_password:
            ttk.Label(self, text="All fields are required. Please fill in all details.", bootstyle="danger").pack(pady=5)
            return

        if not self.is_valid_email(email):
            ttk.Label(self, text="Invalid email format. Please enter a valid email.", bootstyle="danger").pack(pady=5)
            return

        if password != confirm_password:
            ttk.Label(self, text="Passwords do not match. Please try again.", bootstyle="danger").pack(pady=5)
            return

        # Save user to database
        result = db.save_user(email, username, password)
        if "Error" in result:
            ttk.Label(self, text=result, bootstyle="danger").pack(pady=5)
        else:
            success_message = f"Sign Up Successful!\nEmail: {email}\nUsername: {username}. \n Please return to Login Page."
            ttk.Label(self, text=success_message, bootstyle="success").pack(pady=5)
            self.clear_fields()  # Clear form fields after successful signup



