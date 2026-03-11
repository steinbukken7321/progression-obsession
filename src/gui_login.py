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

        # Base Layers
        self.bg_label = ctk.CTkLabel(master, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.card_label = ctk.CTkLabel(master, image=self.card_img, text="")
        self.card_label.place(relx=0.5, rely=0.5, anchor="center")

        self.widgets = []
        self.show_view("login")

    def toggle_password(self, entry, button):
        if entry.cget("show") == "*":
            entry.configure(show="")
            button.configure(text="🔒")
        else:
            entry.configure(show="*")
            button.configure(text="👁")

    def clear_widgets(self):
        for w in self.widgets:
            w.destroy()
        self.widgets = []

    def show_view(self, view_name):
        self.clear_widgets()
        
        if view_name == "login":
            # Título: Letras Soltas (fg_color="transparent" sem frames intermediários resolve)
            title = ctk.CTkLabel(self.master, text="PROGRESSION\nOBSESSION", 
                                 font=("Georgia", 36, "bold"), text_color="#D4AF37", 
                                 fg_color="transparent")
            title.place(relx=0.5, rely=0.25, anchor="center")
            
            # Inputs Quadrados
            email = ctk.CTkEntry(self.master, width=280, height=45, placeholder_text="Soul ID", 
                                 fg_color="#FFFFFF", text_color="#000000", border_color="#000000", 
                                 border_width=1, corner_radius=0)
            email.place(relx=0.5, rely=0.42, anchor="center")
            
            password = ctk.CTkEntry(self.master, width=280, height=45, placeholder_text="Access Code", 
                                    show="*", fg_color="#FFFFFF", text_color="#000000", 
                                    border_color="#000000", border_width=1, corner_radius=0)
            password.place(relx=0.5, rely=0.51, anchor="center")

            eye_btn = ctk.CTkButton(self.master, text="👁", width=35, height=35, 
                                    fg_color="transparent", text_color="#000000", hover=False,
                                    font=("Segoe UI Symbol", 24),
                                    command=lambda: self.toggle_password(password, eye_btn))
            eye_btn.place(relx=0.6, rely=0.51, anchor="center")
            
            # Botões Redondos com Borda Preta
            btn_in = ctk.CTkButton(self.master, text="INITIATE OBSESSION", 
                                   fg_color="#D4AF37", hover_color="#B8860B", text_color="#000000",
                                   width=280, height=55, corner_radius=28, 
                                   border_width=2, border_color="#000000",
                                   font=("Georgia", 16, "bold"), 
                                   command=lambda: self.login_callback(email.get(), password.get()))
            btn_in.place(relx=0.5, rely=0.66, anchor="center")
            
            btn_reg = ctk.CTkButton(self.master, text="CREATE NEW SOUL", 
                                    fg_color="#228B22", hover_color="#006400", text_color="#FFFFFF",
                                    width=280, height=55, corner_radius=28,
                                    border_width=2, border_color="#000000",
                                    font=("Georgia", 16, "bold"), 
                                    command=lambda: self.show_view("register"))
            btn_reg.place(relx=0.5, rely=0.76, anchor="center")
            
            self.widgets.extend([title, email, password, eye_btn, btn_in, btn_reg])

        elif view_name == "register":
            title = ctk.CTkLabel(self.master, text="NEW SOUL\nREGISTRATION", 
                                 font=("Georgia", 26, "bold"), text_color="#D4AF37", 
                                 fg_color="transparent")
            title.place(relx=0.5, rely=0.25, anchor="center")
            
            e_reg = ctk.CTkEntry(self.master, width=280, height=45, placeholder_text="Email", 
                                 fg_color="#FFFFFF", text_color="#000000", border_color="#000000", corner_radius=0)
            e_reg.place(relx=0.5, rely=0.38, anchor="center")
            
            p_reg = ctk.CTkEntry(self.master, width=280, height=45, placeholder_text="Sigil", 
                                 show="*", fg_color="#FFFFFF", text_color="#000000", border_color="#000000", corner_radius=0)
            p_reg.place(relx=0.5, rely=0.47, anchor="center")

            eye_reg = ctk.CTkButton(self.master, text="👁", width=35, height=35, 
                                    fg_color="transparent", text_color="#000000", hover=False,
                                    font=("Segoe UI Symbol", 24), command=lambda: self.toggle_password(p_reg, eye_reg))
            eye_reg.place(relx=0.6, rely=0.47, anchor="center")
            
            c_reg = ctk.CTkEntry(self.master, width=280, height=45, placeholder_text="Confirm Sigil", 
                                 show="*", fg_color="#FFFFFF", text_color="#000000", border_color="#000000", corner_radius=0)
            c_reg.place(relx=0.5, rely=0.56, anchor="center")

            # OLHO NA CONFIRMAÇÃO
            eye_conf = ctk.CTkButton(self.master, text="👁", width=35, height=35, 
                                     fg_color="transparent", text_color="#000000", hover=False,
                                     font=("Segoe UI Symbol", 24), command=lambda: self.toggle_password(c_reg, eye_conf))
            eye_conf.place(relx=0.6, rely=0.56, anchor="center")
            
            btn_f = ctk.CTkButton(self.master, text="FORGE ACCOUNT", fg_color="#228B22", text_color="#FFFFFF", 
                                  width=280, height=55, corner_radius=28, border_width=2, border_color="#000000",
                                  font=("Georgia", 16, "bold"), command=lambda: self.register_callback(e_reg.get(), p_reg.get(), c_reg.get()))
            btn_f.place(relx=0.5, rely=0.71, anchor="center")
            
            btn_b = ctk.CTkButton(self.master, text="GO BACK", fg_color="#8B0000", text_color="#FFFFFF", 
                                  width=280, height=55, corner_radius=28, border_width=2, border_color="#000000",
                                  font=("Georgia", 16, "bold"), command=lambda: self.show_view("login"))
            btn_b.place(relx=0.5, rely=0.81, anchor="center")
            
            self.widgets.extend([title, e_reg, p_reg, eye_reg, c_reg, eye_conf, btn_f, btn_b])