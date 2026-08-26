import os
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login_success=None, on_register_click=None):
        super().__init__(master, fg_color="transparent")
        
        self.on_login_success = on_login_success
        self.on_register_click = on_register_click

        self.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image_raw = None
        self.bg_photo = None
        self.canvas_image_id = None

        self.load_background()
        self.bind("<Configure>", self.on_resize)

        self.card_frame = ctk.CTkFrame(
            self.canvas,
            fg_color="#0D0D0F",
            corner_radius=0,
            border_width=2,
            border_color="#C5A880"
        )
        self.card_window = self.canvas.create_window(0, 0, window=self.card_frame, anchor="center")

        self.title_label = ctk.CTkLabel(
            self.card_frame, 
            text="PROGRESSION OBSESSION", 
            font=("Georgia", 18, "bold"),
            text_color="#F3E5AB"
        )
        self.title_label.pack(padx=40, pady=(30, 20))

        self.entry_user = ctk.CTkEntry(
            self.card_frame,
            placeholder_text="Soul ID",
            font=("Arial", 14),
            width=300,
            corner_radius=0,
            fg_color="#18181C",
            border_color="#3D3832",
            border_width=1,
            text_color="#FFFFFF",
            placeholder_text_color="#7A7570"
        )
        self.entry_user.pack(padx=30, pady=10)

        self.entry_pass = ctk.CTkEntry(
            self.card_frame,
            placeholder_text="Access Code",
            font=("Arial", 14),
            width=300,
            corner_radius=0,
            fg_color="#18181C",
            border_color="#3D3832",
            border_width=1,
            text_color="#FFFFFF",
            placeholder_text_color="#7A7570",
            show="*"
        )
        self.entry_pass.pack(padx=30, pady=10)

        # Label para exibir mensagens de erro ou sucesso na interface
        self.msg_label = ctk.CTkLabel(
            self.card_frame,
            text="",
            font=("Arial", 12),
            text_color="#E74C3C" # Vermelho padrão para erros, muda para verde para sucesso
        )
        self.msg_label.pack(pady=2)

        self.btn_login = ctk.CTkButton(
            self.card_frame,
            text="INITIATE OBSESSION",
            font=("Georgia", 13, "bold"),
            width=300,
            height=42,
            corner_radius=0,
            fg_color="#C5A880",
            hover_color="#D8BA90",
            text_color="#121214",
            command=self.handle_login
        )
        self.btn_login.pack(padx=30, pady=(10, 10))

        self.btn_register = ctk.CTkButton(
            self.card_frame,
            text="CREATE NEW SOUL",
            font=("Georgia", 13, "bold"),
            width=300,
            height=42,
            corner_radius=0,
            fg_color="#1B3826",
            hover_color="#244D34",
            text_color="#D4EDBC",
            command=self.handle_register_redirect
        )
        self.btn_register.pack(padx=30, pady=(0, 25))

    def show_message(self, text, is_error=True):
        color = "#E74C3C" if is_error else "#2ECC71"
        self.msg_label.configure(text=text, text_color=color)

    def load_background(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        img_path = os.path.join(base_path, "assets", "bottomlogin.jpeg")
        
        if os.path.exists(img_path):
            self.bg_image_raw = Image.open(img_path)
            resized = self.bg_image_raw.resize((1000, 700), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    def on_resize(self, event):
        if self.bg_image_raw and event.width > 1 and event.height > 1:
            resized = self.bg_image_raw.resize((event.width, event.height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.itemconfig(self.canvas_image_id, image=self.bg_photo)
            self.canvas.coords(self.card_window, event.width / 2, event.height / 2)

    def handle_login(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        if self.on_login_success:
            self.on_login_success(user, pwd)

    def handle_register_redirect(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        if self.on_register_click:
            self.on_register_click(user, pwd)