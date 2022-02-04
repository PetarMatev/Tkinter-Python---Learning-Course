from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
root.iconbitmap('D:/03. Python/Python Projects/Tkinter Project/Images/Kitchen 1.jpg')
root.geometry("600x100")

# Create a Zipcode Lookup Function

def zipLookup():
    #zip.get()
    zipLabel = Label(root, text=zip.get())
    #zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=76B17D3C-5E80-4237-BCE2-933D55E3B1C8")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = str(api[0]['AQI'])
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_colour = "#0C0"
        elif category == "Modarate":
            weather_colour = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900"
        elif category == "Unhealthy":
            weather_colour = "#FF0000"
        elif category == "Very Unhealthy":
            weather_colour = "#990066"
        elif category == "Hazardous":
            weather_colour = "#660000"

        root.configure(background=weather_colour)

        myLabel = Label(root, text=city + " Air Quality " + quality + " " + category, font=("Helvetica", 20),
                        background=weather_colour)
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error.."


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

Submit_button = Button(root, text="Lookup ZipCode", command=zipLookup)
Submit_button.grid(row=0, column=1)




root.mainloop()
