import os
from dotenv import load_dotenv
from controllers.weather_controller import WeatherController
import tkinter as tk

# Memuat file .env
load_dotenv()

# Mengambil API key dari .env
api_key = os.getenv("OPENWEATHERMAP_API_KEY")

# Pastikan API key berhasil dimuat
if not api_key:
    raise ValueError("API key tidak ditemukan. Pastikan file .env berisi OPENWEATHERMAP_API_KEY=your_api_key_here")

# Inisialisasi Tkinter dan controller
root = tk.Tk()
app = WeatherController(root, api_key)
root.mainloop()