import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk 

class MainPage(ttk.Frame):
    def __init__(self, parent, show_page, session):
        super().__init__(parent)

        self.session = session
        self.show_page = show_page

        # Ensure the frame uses pack layout
        self.pack(fill="both", expand=True)

        # Define the seat, meal, and beverage options as instance attributes
        self.seats = ['Window', 'Aisle', 'Middle']
        self.meals = ['Vegetarian', 'Non-Vegetarian', 'Vegan', 'Gluten-Free']
        self.beverages = ['Water', 'Juice', 'Soda', 'Coffee', 'Tea']

        
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Image section (left side)
        image = Image.open("pages/images/Terminal.jpg")  
        image = image.resize((400, 600))  # Resize as needed
        photo = ImageTk.PhotoImage(image)

        image_label = ttk.Label(container, image=photo)
        image_label.image = photo  
        image_label.pack(side="left", padx=20, pady=20)

        # Form section (right side)
        form_frame = ttk.Frame(container)
        form_frame.pack(side="right", padx=50, pady=20, anchor="e", fill="both", expand=True)

        # Title and input fields
        title_frame = ttk.Frame(form_frame)
        title_frame.pack(pady=20)

        ttk.Label(title_frame, text="Please enter the details below:", font=("Helvetica", 14, "bold")).pack(anchor="center", padx=10)

        ttk.Label(title_frame, text="Name:", font=("Helvetica", 14)).pack(anchor="w", padx=10, pady=(20,5))
        self.name_entry = ttk.Entry(title_frame, bootstyle="primary", width=25)
        self.name_entry.pack(padx=10, pady=(5, 0))

        ttk.Label(title_frame, text="Email:", font=("Helvetica", 14)).pack(anchor="w", padx=10,pady=(10,5))
        self.email_entry = ttk.Entry(title_frame, bootstyle="primary", width=25)
        self.email_entry.pack(padx=10, pady=(5, 0))

        seat_frame = ttk.Frame(form_frame)
        seat_frame.pack(pady=10)
        ttk.Label(seat_frame, text="Seat Preference:", font=("Helvetica", 14)).pack(anchor="w", padx=10, pady=(10,5))
        self.seat_var = ttk.StringVar(value=self.seats[0])
        self.seat_menu = ttk.Combobox(seat_frame, textvariable=self.seat_var, values=self.seats, bootstyle="info", state="readonly")
        self.seat_menu.pack(padx=10, pady=5)

        # Meal Choices
        meal_frame = ttk.Frame(form_frame)
        meal_frame.pack(pady=10)

        ttk.Label(meal_frame, text="Meal Choices:", font=("Helvetica", 14, "bold")).pack(anchor="w", padx=10, pady=(20,5))

        self.selected_meal = ttk.StringVar(value=self.meals[0])

        for meal in self.meals:
            ttk.Radiobutton(
                meal_frame,
                text=meal,
                variable=self.selected_meal,
                value=meal,
                bootstyle="success-round-toggle",
                padding=(8, 2),
            ).pack(anchor="w", padx=10, pady=1)

        # Beverage Choices
        beverage_frame = ttk.Frame(form_frame)
        beverage_frame.pack(pady=10)

        ttk.Label(beverage_frame, text="Beverage Choices:", font=("Helvetica", 14, "bold")).pack(anchor="w", padx=10, pady=5)

        self.selected_beverage = ttk.StringVar(value=self.beverages[0])

        for beverage in self.beverages:
            ttk.Radiobutton(
                beverage_frame,
                text=beverage,
                variable=self.selected_beverage,
                value=beverage,
                bootstyle="info-round-toggle",
                padding=(8, 2),
            ).pack(anchor="w", padx=10, pady=1)

        # Submit and navigation buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(pady=20)
        self.submit_button = ttk.Button(button_frame, text="Continue", command=self.submit_reservation, bootstyle="outline-primary")
        self.submit_button.pack()

    def submit_reservation(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        seat = self.seat_var.get()
        meal_choice = self.selected_meal.get()
        beverage_choice = self.selected_beverage.get()

        if not name or not email or not "@" in email:
            messagebox.showwarning("Input Error", "Please enter a valid name and email.")
            return

        # Store user inputs in the session
        self.session.set("name", name)
        self.session.set("email", email)
        self.session.set("seat_preference", seat)
        self.session.set("meal_choices", meal_choice)
        self.session.set("beverage_choices", beverage_choice)

        # Clear the text fields
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')

        # Reset selections
        self.seat_var.set(self.seats[0])
        self.selected_meal.set(self.meals[0])
        self.selected_beverage.set(self.beverages[0])

        # Navigate to the next page
        self.show_page("ConfirmationPage")
