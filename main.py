from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from weather import get_weather, get_forecast
def display_forecast(forecast_data):

    for widget in forecast_frame.winfo_children():
        widget.destroy()

    forecasts = []

    for forecast in forecast_data["list"]:

        date_time = forecast["dt_txt"]

        if "12:00:00" in date_time:

            forecasts.append(forecast)

    for i, forecast in enumerate(forecasts):

        date = datetime.strptime(
        forecast["dt_txt"],
        "%Y-%m-%d %H:%M:%S"
        ).strftime("%d/%m/%Y")

        temperature = forecast["main"]["temp"]

        weather = forecast["weather"][0]["description"].title()

        rain_probability = forecast["pop"] * 100

        card = tk.Frame(
            forecast_frame,
            bg="white",
            width=105,
            height=130
        )

        card.grid(
            row=0,
            column=i,
            padx=5
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=date,
            font=("Arial", 10, "bold"),
            bg="white"
        ).pack(pady=5)

        tk.Label(
            card,
            text=f"{temperature:.0f}°C",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack()

        tk.Label(
            card,
            text=weather,
            font=("Arial", 9),
            bg="white",
            wraplength=90
        ).pack(pady=3)

        tk.Label(
            card,
            text=f"🌧 {rain_probability:.0f}%",
            font=("Arial", 9),
            bg="white"
        ).pack()

def search_weather():

    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Input Error",
            "Please enter a city name."
        )
        return

    data = get_weather(city)
    forecast_data = get_forecast(city)
    if forecast_data:
        display_forecast(forecast_data)

    if data:

        city_label.config(
            text=f"📍 {data['name']}"
        )

        temperature_label.config(
            text=f"{data['main']['temp']:.1f} °C"
        )

        weather_label.config(
            text=data["weather"][0]["description"].title()
        )

        humidity_value.config(
            text=f"{data['main']['humidity']}%"
        )

        wind_value.config(
            text=f"{data['wind']['speed']} m/s"
        )

        status_label.config(
            text="Weather updated successfully"
        )
    if forecast_data:

        for forecast in forecast_data["list"]:

            date_time = forecast["dt_txt"]

        if "12:00:00" in date_time:

            date = datetime.strptime(
            forecast["dt_txt"],
            "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y")

            temperature = forecast["main"]["temp"]

            weather = forecast["weather"][0]["description"].title()

            rain_probability = forecast["pop"] * 100

            print(
                date,
                temperature,
                weather,
                rain_probability
            )


# Main Window
root = tk.Tk()

root.title("Weather Dashboard")
root.geometry("800x800")
root.resizable(True, True)

root.configure(bg="#EAF4F4")



# Header
header = tk.Frame(
    root,
    bg="#1D3557",
    height=100
)

header.pack(fill="x")

title_label = tk.Label(
    header,
    text="🌤 Raghvendra Parmar-weather dashboard",
    font=("Arial", 26, "bold"),
    bg="#0D2444",
    fg="white"
)

title_label.pack(pady=30)


# Search Section
search_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)

search_frame.pack(pady=25)


city_entry = tk.Entry(
    search_frame,
    font=("Arial", 16),
    width=25
)

city_entry.grid(
    row=0,
    column=0,
    padx=10
)


search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 14, "bold"),
    command=search_weather,
    padx=15,
    pady=5
)

search_button.grid(
    row=0,
    column=1
)


# -----------------------------
# City
# -----------------------------

city_label = tk.Label(
    root,
    text="📍 City",
    font=("Arial", 24, "bold"),
    bg="#EAF4F4"
)

city_label.pack(pady=15)


# -----------------------------
# Temperature
# -----------------------------

temperature_label = tk.Label(
    root,
    text="-- °C",
    font=("Arial", 42, "bold"),
    bg="#EAF4F4"
)

temperature_label.pack(pady=5)


# -----------------------------
# Weather Condition
# -----------------------------

weather_label = tk.Label(
    root,
    text="Weather condition",
    font=("Arial", 18),
    bg="#EAF4F4"
)

weather_label.pack(pady=5)


# -----------------------------
# Information Cards
# -----------------------------

info_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)

info_frame.pack(pady=30)


# Humidity Card

humidity_card = tk.Frame(
    info_frame,
    bg="white",
    width=200,
    height=100
)

humidity_card.grid(
    row=0,
    column=0,
    padx=15
)

humidity_card.pack_propagate(False)


tk.Label(
    humidity_card,
    text="💧 Humidity",
    font=("Arial", 14, "bold"),
    bg="white"
).pack(pady=10)


humidity_value = tk.Label(
    humidity_card,
    text="--",
    font=("Arial", 20, "bold"),
    bg="white"
)

humidity_value.pack()


# Wind Card

wind_card = tk.Frame(
    info_frame,
    bg="white",
    width=200,
    height=100
)

wind_card.grid(
    row=0,
    column=1,
    padx=15
)

wind_card.pack_propagate(False)


tk.Label(
    wind_card,
    text="💨 Wind Speed",
    font=("Arial", 14, "bold"),
    bg="white"
).pack(pady=10)


wind_value = tk.Label(
    wind_card,
    text="--",
    font=("Arial", 20, "bold"),
    bg="white"
)

wind_value.pack()


# -----------------------------
# Status
# -----------------------------

status_label = tk.Label(
    root,
    text="Enter a city to get weather information",
    font=("Arial", 11),
    bg="#EAF4F4"
)

status_label.pack(pady=20)
# -----------------------------
# 5-Day Forecast
# -----------------------------

forecast_title = tk.Label(
    root,
    text="5-Day Forecast",
    font=("Arial", 20, "bold"),
    bg="#EAF4F4"
)

forecast_title.pack(pady=10)


forecast_frame = tk.Frame(
    root,
    bg="#EAF4F4"
)

forecast_frame.pack(pady=10)

# -----------------------------
# Start Application
# -----------------------------

root.mainloop()