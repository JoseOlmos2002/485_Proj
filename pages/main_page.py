import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class MainPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page

        # Ensure the frame uses pack layout
        self.pack(fill="both", expand=True)

        # Seat, meal, and beverage options
        self.seats = ['Window', 'Aisle', 'Middle']
        self.meals = ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Gluten-Free']
        self.beverages = ['Water', 'Juice', 'Soda', 'Coffee', 'Tea']

        # Create and place widgets using pack layout
        title_frame = ttk.Frame(self)
        title_frame.pack(pady=20)
        ttk.Label(title_frame, text="Name:").pack(anchor="w", padx=10)
        self.name_entry = ttk.Entry(title_frame, bootstyle="primary", width=25)
        self.name_entry.pack(padx=10, pady=(5, 0))

        ttk.Label(title_frame, text="Email:").pack(anchor="w", padx=10)
        self.email_entry = ttk.Entry(title_frame, bootstyle="primary", width=25)
        self.email_entry.pack(padx=10, pady=(5, 0))

        seat_frame = ttk.Frame(self)
        seat_frame.pack(pady=10)
        ttk.Label(seat_frame, text="Seat Preference:").pack(anchor="w", padx=10, pady=5)
        self.seat_var = ttk.StringVar(value=self.seats[0])
        self.seat_menu = ttk.Combobox(seat_frame, textvariable=self.seat_var, values=self.seats, bootstyle="info", state="readonly")
        self.seat_menu.pack(padx=10, pady=5)

        # Meal Choices
        meal_frame = ttk.Frame(self)
        meal_frame.pack(pady=10)

        # Meal Choices Label (larger font)
        ttk.Label(meal_frame, text="Meal Choices:", font=("Helvetica", 14, "bold")).pack(anchor="w", padx=10, pady=5)

        # Checkboxes with larger text
        self.meal_vars = {meal: ttk.IntVar() for meal in self.meals}
        for meal in self.meals:
            ttk.Checkbutton(
                meal_frame, 
                text=meal, 
                variable=self.meal_vars[meal], 
                bootstyle="success-round-toggle",
                padding=(8, 2),  # Increase padding for easier interaction
            ).pack(anchor="w", padx=10, pady=1)  # Add slight vertical padding


        # Beverage Choices
        beverage_frame = ttk.Frame(self)
        beverage_frame.pack(pady=10)

        # Beverage Choices Label (larger font)
        ttk.Label(beverage_frame, text="Beverage Choices:", font=("Helvetica", 14, "bold")).pack(anchor="w", padx=10, pady=5)

        # Checkboxes with larger text and better spacing
        self.beverage_vars = {beverage: ttk.IntVar() for beverage in self.beverages}
        for beverage in self.beverages:
            ttk.Checkbutton(
                beverage_frame, 
                text=beverage, 
                variable=self.beverage_vars[beverage], 
                bootstyle="info-round-toggle",
                padding=(8, 2),  # Increase padding for easier interaction
            ).pack(anchor="w", padx=10, pady=1)  # Add slight vertical padding

        # Submit and navigation buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)
        self.submit_button = ttk.Button(button_frame, text="Submit Reservation", command=self.submit_reservation, bootstyle="primary")
        self.submit_button.pack()

    def submit_reservation(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        seat = self.seat_var.get()
        meal_choices = [meal for meal, var in self.meal_vars.items() if var.get()]
        beverage_choices = [bev for bev, var in self.beverage_vars.items() if var.get()]

        

        if not name or not email:
            messagebox.showwarning("Input Error", "Please enter your name and email.")
            return
        
        
        # Store user inputs in the session
        self.session.set("name", name)
        self.session.set("email", email)
        self.session.set("seat_preference", seat)
        self.session.set("meal_choices", meal_choices)
        self.session.set("beverage_choices", beverage_choices)

        # Clear the text fields
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')

        # Reset the selection for combobox and checkbuttons
        self.seat_var.set(self.seats[0])  # Reset to default seat
        for meal in self.meal_vars.values():
            meal.set(0)  # Uncheck all meal options
        for beverage in self.beverage_vars.values():
            beverage.set(0)  # Uncheck all beverage options

        # Navigate to the next page
        self.show_page("ConfirmationPage")



 
