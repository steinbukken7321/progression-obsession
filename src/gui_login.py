import customtkinter as ctk
from PIL import Image
import os

class LoginFrame:
    def __init__(self, master, login_callback, register_callback):
        self.master = master
        self.login_callback = login_callback
        self.register_callback = register_callback

        # --- Assets ---
        current_dir = os.path.dirname(os.path.realpath(__file__))
        assets_path = os.path.join(os.path.dirname(current_dir), "assets")
        
        bg_pil = Image.open(os.path.join(assets_path, "bottomlogin.jpeg"))
        self.bg_img = ctk.CTkImage(bg_pil, size=(1100, 700))
        
        card_pil = Image.open(os.path.join(assets_path, "loginpainel.jpeg"))
        self.card_img = ctk.CTkImage(card_pil, size=(450, 650))

        # --- Camadas de Base ---
        self.bg_label = ctk.CTkLabel(master, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.card_label = ctk.CTkLabel(master, image=self.card_img, text="")
        self.card_label.place(relx=0.5, rely=0.5, anchor="center")

        # Engrenagem
        self.settings_btn = ctk.CTkButton(
            master, text="⚙️", width=40, height=40,
            fg_color="transparent", text_color="black",
            font=ctk.CTkFont(size=28), hover_color=None,
            command=lambda: print("Settings")
        )
        self.settings_btn.place(relx=0.96, rely=0.04, anchor="center")

        self.widgets = []
        self.show_view("login")

    def clear_widgets(self):
        for w in self.widgets:
            w.destroy()
        self.widgets = []

    def show_view(self, view_name):
        self.clear_widgets()
        
        if view_name == "login":
            # Título
            title = ctk.CTkLabel(self.master, text="PROGRESSION\nOBSESSION", 
                                 font=("Georgia", 32, "bold"), text_color="#D4AF37", fg_color="transparent")
            title.place(relx=0.5, rely=0.25, anchor="center")
            
            # Inputs
            email = ctk.CTkEntry(self.master, width=260, height=40, placeholder_text="Soul ID", 
                                 fg_color="#FFFFFF", text_color="#000000", border_color="#D4AF37")
            email.place(relx=0.5, rely=0.42, anchor="center")
            
            password = ctk.CTkEntry(self.master, width=260, height=40, placeholder_text="Access Code", 
                                    show="*", fg_color="#FFFFFF", text_color="#000000", border_color="#D4AF37")
            password.place(relx=0.5, rely=0.50, anchor="center")
            
            # Botão INICIAR (Dourado)
            btn_in = ctk.CTkButton(self.master, text="INITIATE OBSESSION", 
                                   fg_color="#D4AF37", hover_color="#B8860B", text_color="#000000",
                                   width=260, height=50, corner_radius=12,
                                   font=("Georgia", 15, "bold"),
                                   command=lambda: self.login_callback(email.get(), password.get()))
            btn_in.place(relx=0.5, rely=0.65, anchor="center")
            
            # Botão REGISTRO (Verde)
            btn_reg = ctk.CTkButton(self.master, text="CREATE NEW SOUL", 
                                    fg_color="#228B22", hover_color="#006400", text_color="#FFFFFF",
                                    width=260, height=50, corner_radius=12,
                                    font=("Georgia", 15, "bold"),
                                    command=lambda: self.show_view("register"))
            btn_reg.place(relx=0.5, rely=0.74, anchor="center")
            
            self.widgets.extend([title, email, password, btn_in, btn_reg])

        elif view_name == "register":
            title = ctk.CTkLabel(self.master, text="NEW SOUL\nREGISTRATION", 
                                 font=("Georgia", 24, "bold"), text_color="#D4AF37", fg_color="transparent")
            title.place(relx=0.5, rely=0.25, anchor="center")
            
            e_reg = ctk.CTkEntry(self.master, width=260, height=40, placeholder_text="Email", fg_color="#FFFFFF", text_color="#000000", border_color="#D4AF37")
            e_reg.place(relx=0.5, rely=0.38, anchor="center")
            
            p_reg = ctk.CTkEntry(self.master, width=260, height=40, placeholder_text="Sigil", show="*", fg_color="#FFFFFF", text_color="#000000", border_color="#D4AF37")
            p_reg.place(relx=0.5, rely=0.46, anchor="center")
            
            c_reg = ctk.CTkEntry(self.master, width=260, height=40, placeholder_text="Confirm Sigil", show="*", fg_color="#FFFFFF", text_color="#000000", border_color="#D4AF37")
            c_reg.place(relx=0.5, rely=0.54, anchor="center")
            
            # Botão FORGE (Verde)
            btn_f = ctk.CTkButton(self.master, text="FORGE ACCOUNT", 
                                  fg_color="#228B22", hover_color="#006400", text_color="#FFFFFF",
                                  width=260, height=50, corner_radius=12, font=("Georgia", 15, "bold"),
                                  command=lambda: self.register_callback(e_reg.get(), p_reg.get(), c_reg.get()))
            btn_f.place(relx=0.5, rely=0.68, anchor="center")
            
            # Botão VOLTAR (Vermelho)
            btn_b = ctk.CTkButton(self.master, text="GO BACK", 
                                  fg_color="#8B0000", hover_color="#B22222", text_color="#FFFFFF",
                                  width=260, height=50, corner_radius=12, font=("Georgia", 15, "bold"),
                                  command=lambda: self.show_view("login"))
            btn_b.place(relx=0.5, rely=0.77, anchor="center")
            
            self.widgets.extend([title, e_reg, p_reg, c_reg, btn_f, btn_b])