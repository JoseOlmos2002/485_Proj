import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

class MainPage(ttk.Frame):
    def __init__(self, parent, show_page):
        super().__init__(parent)

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
        ttk.Label(meal_frame, text="Meal Choices:").pack(anchor="w", padx=10, pady=5)
        self.meal_vars = {meal: ttk.IntVar() for meal in self.meals}
        for meal in self.meals:
            ttk.Checkbutton(meal_frame, text=meal, variable=self.meal_vars[meal], bootstyle="success-round-toggle").pack(anchor="w", padx=10)

        # Beverage Choices
        beverage_frame = ttk.Frame(self)
        beverage_frame.pack(pady=10)
        ttk.Label(beverage_frame, text="Beverage Choices:").pack(anchor="w", padx=10, pady=5)
        self.beverage_vars = {beverage: ttk.IntVar() for beverage in self.beverages}
        for beverage in self.beverages:
            ttk.Checkbutton(beverage_frame, text=beverage, variable=self.beverage_vars[beverage], bootstyle="info-round-toggle").pack(anchor="w", padx=10)

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

        reservation_details = f"""
        Reservation Confirmation:
        Name: {name}
        Email: {email}
        Seat Preference: {seat}
        Meal Choices: {', '.join(meal_choices) if meal_choices else 'None'}
        Beverage Choices: {', '.join(beverage_choices) if beverage_choices else 'None'}
        """
        messagebox.showinfo("Reservation Confirmed", reservation_details)

    def clear_and_navigate(self, show_page, next_page):
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
        show_page(next_page)
