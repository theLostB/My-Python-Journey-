import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

def fetch_weather(city):
    try:
        api_key = "844577a9e1ef582df45c7ae5a89a195d"  # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the API call was successful
        if response.status_code == 200:
            # Extracting weather information
            weather_info = {
                "Temperature": f"{data['main']['temp']}°C",
                "Feels Like": f"{data['main']['feels_like']}°C",
                "Min Temperature": f"{data['main']['temp_min']}°C",
                "Max Temperature": f"{data['main']['temp_max']}°C",
                "Pressure": f"{data['main']['pressure']} hPa",
                "Humidity": f"{data['main']['humidity']}%",
                "Weather": data['weather'][0]['description']
            }

            # Displaying weather information in GUI
            result_text.delete(1.0, tk.END)  # Clear previous result
            for key, value in weather_info.items():
                result_text.insert(tk.END, f"{key}: {value}\n")
        else:
            messagebox.showerror("Error", f"Failed to fetch weather data: {data['message']}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")

def fetch_weather_click():
    city = city_entry.get()
    fetch_weather(city)

# Create GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

style = ttk.Style()
style.configure("TFrame", background="#e1d8b9")
style.configure("TLabel", background="#e1d8b9", font=("Helvetica", 12))
style.configure("TButton", background="#4caf50", font=("Helvetica", 12), foreground="#ffffff")

frame = ttk.Frame(root)
frame.pack(pady=20)

city_label = ttk.Label(frame, text="Enter city name:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = ttk.Entry(frame)
city_entry.grid(row=0, column=1, padx=10, pady=10)

fetch_button = ttk.Button(frame, text="Fetch Weather", command=fetch_weather_click)
fetch_button.grid(row=1, columnspan=2, padx=10, pady=10)

result_text = tk.Text(root, height=8, width=40, font=("Helvetica", 12))
result_text.pack(pady=20)

root.mainloop()
