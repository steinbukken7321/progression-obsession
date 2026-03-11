import customtkinter as ctk
from src.database import DatabaseManager
from src.gui_login import LoginFrame
from PIL import Image, ImageTk
import os

class ProgressionObsessionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Progression Obsession")
        self.geometry("1100x700")
        self.resizable(False, False)

        assets_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        icon_path = os.path.join(assets_path, "icongame-incremental.jpg")
        
        if os.path.exists(icon_path):
            try:
                img = Image.open(icon_path)
                self.app_icon = ImageTk.PhotoImage(img) 
                self.after(200, lambda: self.iconphoto(False, self.app_icon))
            except Exception as e:
                print(f"System: Icon error - {e}")

        self.db = DatabaseManager()
        self.user_session = None
        self.show_login()

    def show_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.login_interface = LoginFrame(self, self.handle_login, self.handle_registration)

    def handle_login(self, email, password):
        auth_result = self.db.authenticate(email, password)
        if auth_result:
            self.user_session = auth_result
            self.show_main_game()

    def handle_registration(self, email, password, confirm_password):
        register_result = self.db.register_user(email, password, confirm_password)
        if isinstance(register_result, tuple):
            self.show_login()

    def show_main_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        label = ctk.CTkLabel(self, text="DOPAMINE LOADING...", font=("Consolas", 60), text_color="#D4AF37")
        label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = ProgressionObsessionApp()
    app.mainloop()