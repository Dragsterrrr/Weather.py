# Importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # Getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # Base URL from where we extract weather report
    try:
        # This is the complete URL to get weather conditions of a city
        complete_url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(complete_url)  # Requesting the content of the URL
        x = response.json()  # Converting it into JSON 

        if x["cod"] != "404":
            y = x["main"]  # Getting the "main" key from the JSON object

            # Getting the "temp" key of y
            temp = y["temp"]
            temp -= 273  # Converting temperature from Kelvin to Celsius

            # Storing the value of the "pressure" key of y
            pres = y["pressure"]

            # Getting the value of the "humidity" key of y
            hum = y["humidity"]

            # Storing the value of "weather" key in variable z
            z = x["weather"]

            # Getting the corresponding "description"
            weather_desc = z[0]["description"]

            # Combining the above values as a string 
            info = (
                "Weather description for " + cityName + ":" + 
                "\nTemperature: " + str(temp) + "°C" + 
                "\nAtmospheric pressure: " + str(pres) + " hPa" +
                "\nHumidity: " + str(hum) + "%" +
                "\nDescription: " + str(weather_desc)
            )

            # Showing the weather information in a message box
            mb.showinfo("Weather Report", info)

        else:
            mb.showerror('Error', 'City Not Found!')
    
    except Exception as e:
        mb.showerror('Error', str(e))  # Show pop-up message if any error occurs

# Creating the main window
wn = Tk()
wn.title("Weather Notifier")
wn.geometry('400x300')  # Set window size
wn.config(bg='#f0f8ff')  # Set a light background color

# Title label
title_label = Label(wn, text="Weather Notifier", font=('Helvetica', 18, 'bold'), fg='#333', bg='#f0f8ff')
title_label.pack(pady=10)

# Getting the place name 
label = Label(wn, text='Enter the Location:', font=("Helvetica", 12), bg='#f0f8ff')
label.pack(pady=5)

place = StringVar(wn)
place_entry = Entry(wn, width=30, font=("Helvetica", 12), textvariable=place)
place_entry.pack(pady=10)

# Button to get weather report
btn = Button(wn, text='Get Weather Report', font=('Helvetica', 12, 'bold'), fg='white', bg='#007bff', command=getNotification)
btn.pack(pady=20)

# Run the window until closed by user
wn.mainloop()
