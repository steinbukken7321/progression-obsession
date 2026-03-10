import customtkinter as ctk
from src.database import DatabaseManager
from src.gui_login import LoginFrame # We will create this next
import os

class ProgressionObsessionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Progression Obsession - Professional Build")
        self.geometry("1100x700")
        self.resizable(False, False)

        # Initialize Database Manager
        self.db = DatabaseManager()

        # Current session data
        self.user_session = None

        # Show Login Screen by default
        self.show_login()

    def show_login(self):
        # We will implement the LoginFrame in gui_login.py next
        # For now, let's just confirm the structure is working
        print("System: Waiting for gui_login.py implementation...")

if __name__ == "__main__":
    app = ProgressionObsessionApp()
    app.mainloop()