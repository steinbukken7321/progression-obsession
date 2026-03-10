import customtkinter as ctk
from PIL import Image
import os

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, login_callback, **kwargs):
        super().__init__(master, **kwargs)
        
        self.login_callback = login_callback # Function to call on login
        self.configure(fg_color="transparent") # Make frame invisible to see BG

        # 1. Load Background Image (bottomlogin.jpeg)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        # Go up one level to 'assets'
        bg_path = os.path.join(os.path.dirname(current_dir), "assets", "bottomlogin.jpeg")
        
        bg_image_pil = Image.open(bg_path)
        self.bg_image = ctk.CTkImage(light_image=bg_image_pil,
                                     dark_image=bg_image_pil,
                                     size=(1100, 700))

        # Background Label (covers the whole window)
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 2. Login Box (Glassmorphism effect)
        self.glass_frame = ctk.CTkFrame(self, width=350, height=450, corner_radius=20)
        self.glass_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = ctk.CTkLabel(self.glass_frame, text="PROGRESSION\nOBSESSION", 
                                        font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=40)

        # Inputs
        self.email_entry = ctk.CTkEntry(self.glass_frame, width=280, height=45, placeholder_text="Email Address")
        self.email_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(self.glass_frame, width=280, height=45, placeholder_text="Password", show="*")
        self.pass_entry.pack(pady=10)

        # Login Button
        self.login_btn = ctk.CTkButton(self.glass_frame, text="ENTER THE VOID", 
                                       width=280, height=50, font=ctk.CTkFont(size=15, weight="bold"),
                                       command=self.on_login_press)
        self.login_btn.pack(pady=40)

    def on_login_press(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        # Call the handle_login function in main.py
        self.login_callback(email, password)