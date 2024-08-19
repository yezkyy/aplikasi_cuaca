from models.weather_model import WeatherModel
from views.main_view import MainView
import tkinter as tk
from PIL import Image, ImageTk
import io
import requests

class WeatherController:
    def __init__(self, root, api_key):
        self.model = WeatherModel(api_key)
        self.view = MainView(root)
        self.view.get_weather_button.config(command=self.fetch_weather)

    def fetch_weather(self):
        city_name = self.view.city_entry.get()
        data = self.model.get_weather_data(city_name)

        if data.get("cod") != "404":
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            coord = data["coord"]

            temp = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_description = weather["description"]
            wind_speed = wind["speed"]
            temp_min = main["temp_min"]
            temp_max = main["temp_max"]
            latitude = coord["lat"]
            longitude = coord["lon"]

            result_text = (f"Suhu: {temp}°C\n"
                        f"Tekanan: {pressure} hPa\n"
                        f"Kelembaban: {humidity}%\n"
                        f"Deskripsi: {weather_description.capitalize()}\n"
                        f"Kecepatan Angin: {wind_speed} m/s\n"
                        f"Latitude: {latitude}\n"
                        f"Longitude: {longitude}")

            try:
                # Mendapatkan ikon cuaca
                icon_code = weather["icon"]
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                icon_response = requests.get(icon_url)
                icon_response.raise_for_status()  # Periksa apakah ada kesalahan saat mengambil gambar
                icon_data = icon_response.content
                icon_image = Image.open(io.BytesIO(icon_data))
                icon_photo = ImageTk.PhotoImage(icon_image)
                
                self.view.icon_photo = icon_photo  # Hindari garbage collection
                self.view.set_weather_display(result_text, icon_photo)

            except Exception as e:
                tk.messagebox.showerror("Error", f"Gagal memuat ikon cuaca: {str(e)}")

        else:
            # Menampilkan pesan kesalahan sederhana tanpa argumen ikon
            tk.messagebox.showerror("Kota Tidak Ditemukan", "Kota yang Anda masukkan tidak ditemukan.")