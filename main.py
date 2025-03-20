import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.sign_up import SignupPage
from pages.flight_choice import LocationSelectionPage
from pages.session import Session
from pages.confirmation import ConfirmationPage

class MultiPageApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Flight Reservation")

        screen_width = 1000
        screen_height = 1000

        self.geometry(f"{screen_width}x{screen_height}")

        self.session = Session()

        self.pages = {}
        self.create_pages()

        # Start with the Login page
        self.show_page("LoginPage")

    def create_pages(self):
        # Store pages in a dictionary
        self.pages["MainPage"] = MainPage(self, self.show_page, self.session)
        self.pages["LoginPage"] = LoginPage(self, self.show_page, self.session)
        self.pages["LocationSelectionPage"] = LocationSelectionPage(self, self.show_page, self.session)
        self.pages["SignupPage"] = SignupPage(self, self.show_page)
        self.pages["ConfirmationPage"] = ConfirmationPage(self, self.show_page, self.session)

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(fill="both", expand=True)

        # If the page is LocationSelectionPage and the email has changed, update it
        if page_name == "LocationSelectionPage":
            self.pages[page_name].update_username_display()

        if page_name == "ConfirmationPage":
            self.pages[page_name].update_confirmation_display()

        self.after(50, self._force_redraw)

    def _force_redraw(self):
        # This ensures Tkinter processes the layout updates
        self.update_idletasks()  # Processes pending layout tasks
        self.update()  # Forces a redraw

if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
