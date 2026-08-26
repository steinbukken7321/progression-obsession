import os
from PIL import Image
import customtkinter as ctk

class GameSelectionFrame(ctk.CTkFrame):
    def __init__(self, master, on_class_selected=None):
        super().__init__(master, fg_color="#121214")
        self.on_class_selected = on_class_selected

        self.pack(fill="both", expand=True)

        self.title_label = ctk.CTkLabel(
            self,
            text="CHOOSE YOUR OBSESSION PATH",
            font=("Georgia", 22, "bold"),
            text_color="#F3E5AB"
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Select your class to begin the incremental progression.",
            font=("Arial", 13),
            text_color="#9A9590"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # Container dos Cards de Classes
        self.cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_frame.pack(pady=10)

        # 4 Classes mapeadas com seus respectivos ícones
        classes_data = [
            {
                "name": "ARCHER",
                "icon": "iconarcher.png",
                "desc": "Focuses on precision, speed, and critical multipliers over time."
            },
            {
                "name": "ASSASSIN",
                "icon": "iconassassin.png",
                "desc": "Specializes in burst progression, stealth gains, and hidden multipliers."
            },
            {
                "name": "WARRIOR",
                "icon": "iconwarrior.png",
                "desc": "Relies on raw power, defensive resilience, and steady passive generation."
            },
            {
                "name": "MAGE",
                "icon": "iconmage.png",
                "desc": "Channels arcane energy, accelerating exponential multipliers and resource flow."
            }
        ]

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        assets_dir = os.path.join(base_path, "assets")

        for c_data in classes_data:
            card = ctk.CTkFrame(
                self.cards_frame,
                fg_color="#0D0D0F",
                border_width=2,
                border_color="#C5A880",
                width=230,
                height=420,
                corner_radius=0
            )
            card.pack(side="left", padx=10)
            card.pack_propagate(False)

            icon_path = os.path.join(assets_dir, c_data["icon"])
            img_tk = None
            if os.path.exists(icon_path):
                pil_img = Image.open(icon_path).resize((90, 90), Image.Resampling.LANCZOS)
                img_tk = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(90, 90))

            lbl_icon = ctk.CTkLabel(card, text="", image=img_tk)
            lbl_icon.image = img_tk
            lbl_icon.pack(pady=(25, 15))

            lbl_name = ctk.CTkLabel(
                card,
                text=c_data["name"],
                font=("Georgia", 15, "bold"),
                text_color="#F3E5AB"
            )
            lbl_name.pack(pady=5)

            lbl_desc = ctk.CTkLabel(
                card,
                text=c_data["desc"],
                font=("Arial", 11),
                text_color="#C2BCB5",
                wraplength=200,
                justify="center"
            )
            lbl_desc.pack(pady=10, padx=10)

            btn_select = ctk.CTkButton(
                card,
                text=f"SELECT",
                font=("Georgia", 12, "bold"),
                fg_color="#C5A880",
                hover_color="#D8BA90",
                text_color="#121214",
                corner_radius=0,
                command=lambda name=c_data["name"]: self.select_class(name)
            )
            btn_select.pack(side="bottom", pady=25)

    def select_class(self, class_name):
        if self.on_class_selected:
            self.on_class_selected(class_name)