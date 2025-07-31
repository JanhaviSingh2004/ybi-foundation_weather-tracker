import pandas as pd
from datetime import datetime

weather_data = []
unique_dates = set()

def add_weather(date, temperature, condition):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        if date in unique_dates:
            print("❌ Entry for this date already exists.")
            return
        weather_data.append({
            'Date': date,
            'Temperature': temperature,
            'Condition': condition
        })
        unique_dates.add(date)
        print("✅ Data added successfully!")
    except ValueError:
        print("⚠️ Invalid date format. Use YYYY-MM-DD.")

def show_data():
    if not weather_data:
        print("No data available.")
        return
    df = pd.DataFrame(weather_data)
    print(df)

def summarize_data():
    if not weather_data:
        print("No data to summarize.")
        return
    df = pd.DataFrame(weather_data)
    df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
    print("📊 Average Temperature:", df['Temperature'].mean())
    print("\n🌦️ Condition Count:\n", df['Condition'].value_counts())

def export_to_csv(filename="weather_data.csv"):
    if not weather_data:
        print("No data to export.")
        return
    df = pd.DataFrame(weather_data)
    df.to_csv(filename, index=False)
    print(f"📁 Data exported to {filename}")

add_weather("2025-07-06", 32, "Sunny")
add_weather("2025-07-07", 28, "Rainy")
add_weather("2025-07-06", 30, "Cloudy")

show_data()
summarize_data()
export_to_csv()
