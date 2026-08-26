import customtkinter as ctk
from src.database import DatabaseManager
from src.gui_login import LoginFrame
from src.gui_game import GameSelectionFrame
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
        self.user_session = None # Armazenará (id, username, character_class)
        self.show_login()

    def show_login(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.login_interface = LoginFrame(self, self.handle_login, self.handle_registration)

    def handle_login(self, username, password):
        if not username or not password:
            self.login_interface.show_message("Preencha todos os campos.", is_error=True)
            return

        auth_result = self.db.authenticate(username, password)
        if auth_result:
            self.user_session = auth_result # (id, username, character_class)
            user_id, username_db, saved_class = self.user_session

            # Se o usuário já escolheu uma classe anteriormente, vai direto para o jogo
            if saved_class:
                self.start_incremental_game(saved_class)
            else:
                self.show_class_selection() # Senão, manda escolher
        else:
            self.login_interface.show_message("Soul ID ou Access Code incorretos.", is_error=True)

    def handle_registration(self, username, password):
        success, message = self.db.register_user(username, password)
        if success:
            self.login_interface.show_message(message, is_error=False)
        else:
            self.login_interface.show_message(message, is_error=True)

    def show_class_selection(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.game_selection = GameSelectionFrame(self, on_class_selected=self.save_and_start_game)

    def save_and_start_game(self, chosen_class):
        if self.user_session:
            user_id = self.user_session[0]
            # Salva no banco de dados para não precisar escolher de novo
            self.db.save_user_class(user_id, chosen_class)
            # Atualiza a sessão local
            self.user_session = (user_id, self.user_session[1], chosen_class)
        
        self.start_incremental_game(chosen_class)

    def start_incremental_game(self, chosen_class):
        for widget in self.winfo_children():
            widget.destroy()
        
        label = ctk.CTkLabel(
            self, 
            text=f"OBSESSION INITIALIZED\nCLASS: {chosen_class}\n\n[Incremental Loop Loading...]", 
            font=("Consolas", 24), 
            text_color="#D4AF37",
            justify="center"
        )
        label.place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = ProgressionObsessionApp()
    app.mainloop()