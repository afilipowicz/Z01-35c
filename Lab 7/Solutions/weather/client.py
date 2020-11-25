import matplotlib.pyplot as plt
import requests
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from geopy.geocoders import Nominatim
import json
from datetime import datetime
from PIL import Image,ImageTk
import shutil

def plot(data):
    plt.style.use("ggplot")
    plt.clf()

    x = list(map(lambda x: x[0], data))
    temps = list(map(lambda x: x[1], data))

    plt.bar(x, temps, color="blue")
    plt.title("Hourly forecast")
    plt.xticks(x, x)
    plt.draw()
    fig = plt.gcf()

    canvas = FigureCanvasTkAgg(fig, master=hourlyFrame)
    canvas.draw()

    canvas.get_tk_widget().grid(row=1, sticky="w")

def getWeatherData():
    locationName = city.get()
    geolocator = Nominatim(user_agent="Weather")
    location = geolocator.geocode(locationName)

    parameters = {"lat": location.latitude,
                  "lon": location.longitude,
                  "exclude": ["minutely", "alerts"],
                  "units": "metric",
                  "appid": "820fd123bde0f0772e98a50f46d53262"}
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    responseDict = response.json()

    daily = responseDict["daily"]
    hourly = responseDict["hourly"]

    def getDayData(day):
        date = datetime.fromtimestamp(day["dt"])
        temp = day["temp"]["day"]
        icon = day["weather"][0]["icon"]
        wind = day["wind_speed"]

        hours = filter(lambda hour: datetime.fromtimestamp(hour["dt"]).day == date.day, hourly)
        hourData = list(map(lambda hour: (datetime.fromtimestamp(hour["dt"]).hour, hour["temp"]), hours))

        return (f"{date.day}.{date.month}", temp, icon, wind, hourData)

    dayData = list(map(getDayData, daily[:3]))
    displayDaily(dayData)

    gui.geometry("500x300")
    gui.update()

def displayDaily(data):
    for i, day in enumerate(data):
        dayWidget = DayWidget(forecastFrame, day, width=200, height=200)
        dayWidget.grid(row=1, column=i, padx=(20, 20))

def displayHourly(data):
    plot(data)
    gui.geometry("600x700")
    gui.update()

def getImage(name):
    imageUrl = f"http://openweathermap.org/img/wn/{name}@2x.png"
    filename = imageUrl.split("/")[-1]

    request = requests.get(imageUrl, stream=True)
    request.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(request.raw, f)
    img = Image.open(filename)
    img.resize((50,50), Image.ANTIALIAS)

    return ImageTk.PhotoImage(img)

class DayWidget(Frame):
    def __init__(self, parent, day, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.title = Label(self, text=day[0])
        self.temp = Label(self, text=f"{day[1]}℃")
        img = getImage(day[2])
        self.image = Label(self, image=img)
        self.image.image = img
        self.wind = Label(self, text=f"{day[3]} m/s")
        self.button = Button(self, text="details", command=lambda: displayHourly(day[4]))

        self.title.pack(side="top")
        self.temp.pack(side="top")
        self.image.pack(side="top")
        self.wind.pack(side="top")
        self.button.pack(side="top")

gui = Tk()
gui.title("Weather")
gui.geometry("300x50")

searchFrame = Frame(gui)
forecastFrame = Frame(gui)
hourlyFrame = Frame(gui)

searchFrame.pack(side="top", fill="x")
forecastFrame.pack(fill="both")
hourlyFrame.pack(side="bottom", fill="x")

city = Entry(searchFrame)
searchButton = Button(searchFrame, text="Search", command=getWeatherData)
city.pack(side="left")
searchButton.pack(side="left", padx = (10,10), ipadx = (10))

gui.mainloop()
