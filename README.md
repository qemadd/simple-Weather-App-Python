# Simple Weather App (Python) 🌤️

A command-line Python application that fetches and displays real-time weather data for any user-specified city. This project was developed as part of a University Computer Science Lab assessment to demonstrate proficiency in Python, API integration, and control flow.

# Features
* **Real-Time Data:** Fetches live weather conditions using the OpenWeatherMap API.
* **Interactive Loop:** Allows users to search for multiple cities consecutively without restarting the program.
* **Data Extraction:** Parses JSON responses to extract and display temperature (°C), humidity (%), and weather descriptions.
* **Error Handling:** Gracefully handles invalid inputs or unfound cities.

##  Technologies Used
* **Language:** Python 3
* **Libraries:** `requests`
* **API:** [OpenWeatherMap](https://openweathermap.org/)

###  How to Run
1. Clone this repository to your local machine.
2. Sign up at OpenWeatherMap to get your free API key.
3. Open `simple-Weather-App-Python.py` and replace `"YOUR_API_KEY_HERE"` with your actual API key.
4. Run the script in your terminal:
   ```bash
   python simple-Weather-App-Python.py
