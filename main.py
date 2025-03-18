import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.sign_up import SignupPage
from pages.flight_choice import LocationSelectionPage

class MultiPageApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Flight Reservation")

        screen_width = 1000
        screen_height = 1000

        self.geometry(f"{screen_width}x{screen_height}")

        self.pages = {}
        self.create_pages()

        # Start with the Login page
        self.show_page("LoginPage")

    def create_pages(self):
        # Store pages in a dictionary
        self.pages["MainPage"] = MainPage(self, self.show_page)
        self.pages["LoginPage"] = LoginPage(self, self.show_page)
        self.pages["LocationSelectionPage"] = LocationSelectionPage(self, self.show_page)
        self.pages["SignupPage"] = SignupPage(self, self.show_page)

    def show_page(self, page_name):
        # Hide all pages first
        for page in self.pages.values():
            page.pack_forget()

        # Show the requested page
        self.pages[page_name].pack(fill="both", expand=True)

        # Force a redraw of the window (using after to give Tkinter time to process)
        self.after(50, self._force_redraw)

    def _force_redraw(self):
        # This ensures Tkinter processes the layout updates
        self.update_idletasks()  # Processes pending layout tasks
        self.update()  # Forces a redraw

if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
