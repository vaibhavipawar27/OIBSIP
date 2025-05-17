import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import geocoder
import io

API_KEY = '610a622f2e77d8bc0c07509619c3ce82'

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    data = get_weather(city)
    if data:
        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        icon_id = data['weather'][0]['icon']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']

        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        icon_img = requests.get(icon_url).content
        icon = ImageTk.PhotoImage(Image.open(io.BytesIO(icon_img)))

        icon_label.config(image=icon)
        icon_label.image = icon

        result = f"🌡️ Temp: {temp}°C\n📝 {weather} - {description}\n💨 Wind: {wind} m/s\n💧 Humidity: {humidity}%"
        result_label.config(text=result)
    else:
        messagebox.showerror("Error", "Could not retrieve weather data.")

def detect_location():
    location = geocoder.ip('me')
    if location.ok:
        city_entry.delete(0, tk.END)
        city_entry.insert(0, location.city)
        show_weather()
    else:
        messagebox.showerror("Location Error", "Unable to detect location.")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="#e6f2ff")

tk.Label(root, text="🌤️Weather App   🌤️", font=("Helvetica", 16, "bold"), bg="#e6f2ff").pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=25, justify='center')
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=show_weather, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Use Current Location", command=detect_location, bg="#2196F3", fg="white").pack(pady=5)

icon_label = tk.Label(root, bg="#e6f2ff")
icon_label.pack(pady=10)

result_label = tk.Label(root, font=("Arial", 12), bg="#e6f2ff", justify="center")
result_label.pack()

root.mainloop()
