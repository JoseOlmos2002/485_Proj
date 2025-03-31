import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.sign_up import SignupPage
from pages.flight_choice import LocationSelectionPage
from pages.session import Session
from pages.confirmation import ConfirmationPage
from pages.congratulations import Congratulations
from pages.check_flight import CheckFlight
from pages.flight_details import FlightDetailsPage

class MultiPageApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Flight Reservation")

        screen_width = 850
        screen_height = 800

        self.geometry(f"{screen_width}x{screen_height}")

        self.maxsize(screen_width, screen_height)
        
        self.minsize(screen_width, screen_height)


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
        self.pages["Congratulations"] = Congratulations(self, self.show_page, self.session)
        self.pages["CheckFlight"] = CheckFlight(self, self.show_page, self.session)
        self.pages["FlightDetailsPage"] = FlightDetailsPage(self, self.show_page, self.session)

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()

        self.pages[page_name].pack(fill="both", expand=True)

        if page_name == "LocationSelectionPage":
            self.pages[page_name].update_username_display()

        if page_name == "ConfirmationPage":
            self.pages[page_name].update_confirmation_display()

        if page_name == "Congratulations":
            self.pages[page_name].update_congratulations_display()
        
        if page_name == "FlightDetailsPage":
            self.pages[page_name].update_flight_details()

        self.after(50, self._force_redraw)

    def _force_redraw(self):
        self.update_idletasks() 
        self.update()  

if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
