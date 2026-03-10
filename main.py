import customtkinter as ctk
from src.database import DatabaseManager
from src.gui_login import LoginFrame

class ProgressionObsessionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Progression Obsession - Professional Build")
        self.geometry("1100x700")
        self.resizable(False, False)

        # Init Database
        self.db = DatabaseManager()
        self.user_session = None

        # Container for screens
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.show_login()

    def show_login(self):
        # Create the login frame and pass handle_login as callback
        self.login_view = LoginFrame(self.container, self.handle_login)
        self.login_view.pack(fill="both", expand=True)

    def handle_login(self, email, password):
        # Use the database manager to authenticate
        auth_result = self.db.authenticate(email, password)
        
        if isinstance(auth_result, tuple): # Success (returns user row)
            self.user_session = auth_result
            print(f"System: Access granted to {email}")
            self.login_view.destroy()
            self.show_main_game()
        else:
            print("System: Authentication failed.")

    def show_main_game(self):
        # We will implement gui_game.py in the next session
        print(f"Loading Game UI for {self.user_session[1]}...")
        label = ctk.CTkLabel(self.container, text="DOPAMINE LOADING...", font=("Consolas", 60))
        label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = ProgressionObsessionApp()
    app.mainloop()