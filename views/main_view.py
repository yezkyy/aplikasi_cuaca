import tkinter as tk
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Cuaca")
        self.root.geometry("800x600")
        self.root.config(bg="#E1F5FE")

        self.style = ttk.Style()
        self.style.configure("TLabel", background="#E1F5FE", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12), padding=10)
        self.style.configure("TFrame", background="#E1F5FE")

        self.create_widgets()

    def create_widgets(self):
        # Sidebar/NAVBAR
        self.sidebar = tk.Frame(self.root, width=200, bg="#29B6F6", height=600, padx=10, pady=10, relief="raised")
        self.sidebar.pack_propagate(False)
        self.sidebar.pack(side="left", fill="y")

        # Menambahkan menu ke sidebar
        self.home_button = ttk.Button(self.sidebar, text="Beranda", command=lambda: print("Beranda"), width=15)
        self.home_button.pack(pady=10)

        self.about_button = ttk.Button(self.sidebar, text="Tentang", command=lambda: print("Tentang"), width=15)
        self.about_button.pack(pady=10)

        # Konten Utama
        self.content_frame = tk.Frame(self.root, bg="#E1F5FE")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.header_label = ttk.Label(self.content_frame, text="Aplikasi Cuaca", font=("Arial", 20, "bold"), background="#29B6F6", foreground="white")
        self.header_label.pack(pady=20, fill="x")

        self.city_frame = tk.Frame(self.content_frame, bg="#E1F5FE")
        self.city_frame.pack(pady=20)

        self.city_label = ttk.Label(self.city_frame, text="Masukkan Nama Kota:", font=("Arial", 12))
        self.city_label.pack(side="left")

        self.city_entry = ttk.Entry(self.city_frame, width=30, font=("Arial", 12))
        self.city_entry.pack(side="left", padx=10)

        self.get_weather_button = ttk.Button(self.content_frame, text="Dapatkan Cuaca", command=None)  # Placeholder command
        self.get_weather_button.pack(pady=20)

        self.icon_label = tk.Label(self.content_frame, bg="#E1F5FE")
        self.icon_label.pack(pady=10)

        self.result_label = ttk.Label(self.content_frame, text="", font=("Arial", 14), wraplength=400)
        self.result_label.pack(pady=20)

        self.footer_label = ttk.Label(self.content_frame, text="Powered by OpenWeatherMap", font=("Arial", 10, "italic"))
        self.footer_label.pack(side="bottom", pady=10)

    def set_weather_display(self, text, icon_image):
        self.result_label.config(text=text)
        self.icon_label.config(image=icon_image)
        self.icon_label.image = icon_image
