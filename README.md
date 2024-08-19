# Aplikasi Cuaca

Aplikasi Cuaca ini dibangun menggunakan Python dengan framework Tkinter untuk antarmuka grafis pengguna (GUI). Aplikasi ini memungkinkan pengguna untuk mencari dan melihat informasi cuaca dari berbagai kota di seluruh dunia. Data cuaca diperoleh melalui API dari OpenWeatherMap.

## Fitur
- **Pencarian Cuaca:** Pengguna dapat memasukkan nama kota untuk mendapatkan informasi cuaca seperti suhu, tekanan, kelembaban, deskripsi cuaca, kecepatan angin, dan koordinat geografis (latitude dan longitude).
- **Ikon Cuaca:** Aplikasi menampilkan ikon cuaca yang relevan berdasarkan kondisi cuaca yang dilaporkan.
- **Pesan Kesalahan:** Jika kota tidak ditemukan, aplikasi akan menampilkan popup kesalahan dengan ikon X.
- **Animasi Fade-In:** Deskripsi cuaca ditampilkan dengan efek animasi fade-in.
- **Struktur MVC:** Aplikasi ini diorganisasikan menggunakan arsitektur Model-View-Controller (MVC).

## Instalasi
1. **Clone repository:**
   ```bash
   git clone https://github.com/yezkyy/aplikasi_cuaca.git
   cd weather-app
   ```
2. **Buat virtual environment dan aktifkan:**
   ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/Mac
    venv\Scripts\activate  # Untuk Windows
   ```
3. **Instal dependensi:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Konfigurasi API Key:**
   - Buat file .env di root direktori.
   - Tambahkan API Key Anda dari OpenWeatherMap:
   ```bash
    OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

## Struktur Folder
   ```bash
  weather-app/
  │
  ├── controllers/
  │   └── weather_controller.py    # Logika aplikasi dan interaksi antara model dan view
  │
  ├── models/
  │   └── weather_model.py         # Berisi logika untuk mengambil data dari OpenWeatherMap API
  │
  ├── views/
  │   └── main_view.py             # Menyediakan antarmuka grafis menggunakan Tkinter
  │
  ├── .env                         # File lingkungan untuk menyimpan API key
  ├── .gitignore                   # File yang menentukan file mana yang harus diabaikan Git
  ├── main.py                      # File utama untuk menjalankan aplikasi
  └── requirements.txt             # Daftar dependensi yang diperlukan aplikasi
   ```
