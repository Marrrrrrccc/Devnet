from tkinter import END, BOTH
from tkinter import StringVar
from tkinter.ttk import Label, Button, Frame
import tkinter as tk
# importing get from requests module for API calls
from requests import get
# Initial method to get Information


def getInformation():
    loc = get('https://ipapi.co/json/')  # Fetching data from the api
    ip = loc.json()  # Formatting to json format

    # referencing global variables
    global currentLoc
    global currentLoc
    global publicIP
    global specificIP
    global serviceProvider
    global currency
    global languages
    global asn
    global timezone
    global zipCode
    global capital
    global population

    # checks if API is available
    try:
        # setting variable information
        currentLoc.set(
            'Current Location: ' +
            ip['city'] +
            ", " +
            ip['region'] +
            ", " +
            ip['country_name'])
        publicIP.set('Public IP Address: ' + ip['ip'])
        specificIP = ip['ip']
        serviceProvider.set('Internet Service Provider: ' + ip['org'])
        currency.set('Currency: ' + ip['currency_name'])
        languages.set('Languages: ' + ip['languages'])
        asn.set('Autonomouss System Number: ' + ip['asn'])
        timezone.set('Timezone: ' + ip['timezone'])
        zipCode.set('Zipcode: ' + ip['postal'])
        capital.set("Country's Capital: " + ip['country_capital'])
        population.set("Country's Population: " +
                       str(ip['country_population']))
    except BaseException:
        currentLoc.set("Invalid IP address/Number of API calls Exceeded. "
                       "Please try again later. \nThis Program was made by: "
                       "\n\tMarc Ricson Ricafort\n\tStanley Orong III\n\tCyril Ken Verdad\n\tFrom 4-ITG")
        publicIP.set("")
        serviceProvider.set("")
        currency.set("")
        languages.set("")
        asn.set("")
        timezone.set("")
        zipCode.set("")
        capital.set("")
        population.set("")


# Get information from custom IP
def getCustomInformation():  # onclick function
    newIP = str(customIP.get())
    # Fetching data from the api
    loc = get('https://ipapi.co/' + newIP + '/json')
    ip = loc.json()  # Formatting to json format

    # referencing global variables
    global currentLoc
    global currentLoc
    global publicIP
    global specificIP
    global serviceProvider
    global currency
    global languages
    global asn
    global timezone
    global zipCode
    global capital
    global population

    # checks if API is available
    try:
        # setting variable information
        currentLoc.set(
            'Current Location: ' +
            ip['city'] +
            ", " +
            ip['region'] +
            ", " +
            ip['country_name'])
        publicIP.set('Public IP Address: ' + ip['ip'])
        specificIP = ip['ip']
        serviceProvider.set('Internet Service Provider: ' + ip['org'])
        currency.set('Currency: ' + ip['currency_name'])
        languages.set('Languages: ' + ip['languages'])
        asn.set('Autonomouss System Number: ' + ip['asn'])
        timezone.set('Timezone: ' + ip['timezone'])
        zipCode.set('Zipcode: ' + ip['postal'])
        capital.set("Country's Capital: " + ip['country_capital'])
        population.set("Country's Population: " +
                       str(ip['country_population']))
    except BaseException:
        currentLoc.set("Invalid IP address/Number of API calls Exceeded."
                       " Please try again later. \nThis Program was made by: "
                       "\n\tMarc Ricson Ricafort\n\tStanley Orong III\n\tCyril Ken Verdad\n\tFrom 4-ITG")
        publicIP.set("")
        serviceProvider.set("")
        currency.set("")
        languages.set("")
        asn.set("")
        timezone.set("")
        zipCode.set("")
        capital.set("")
        population.set("")

# Sets a placeholder var


def placeholder(event, text):
    text.configure(state='normal')
    text.delete('0', END)


# Clears the Entry Text
def clearText():
    customIP.delete('0', END)


# main
window = tk.Tk()
window.title('IPGetR')
header = StringVar()  # message textvariable
window.resizable(0, 0)  # Sets the window to unresizable
window.geometry('570x700')  # Adds a fixed width and height
# Frame used to add virtual padding between window and text
innerWindow = Frame(window, relief='sunken')
innerWindow.pack(fill=BOTH, expand=True, padx=75, pady=20)

# variables
currentLoc = StringVar()
publicIP = StringVar()
serviceProvider = StringVar()
currency = StringVar()
languages = StringVar()
asn = StringVar()
timezone = StringVar()
zipCode = StringVar()
capital = StringVar()
population = StringVar()
specificIP = ""

# Method to get initial information
getInformation()

#label/ message (static)
# Title
Label(
    innerWindow,
    text="Welcome to IPGetR",
    font=(
        "Helvetica bold",
         25)).pack()
Label(
    innerWindow,
    text="The program where you can get information from your IP!  ",
    font=(
        "Helvetica",
         14)).pack()
Label(
    innerWindow,
    text='\n\nYour Information',
    font=(
        "Helvetica bold",
        14),
    anchor='w').pack(
    fill='both')

# Content
Label(
    innerWindow,
    textvariable=currentLoc,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=publicIP,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=serviceProvider,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=currency,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=languages,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=asn,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=timezone,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=zipCode,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=capital,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
Label(
    innerWindow,
    textvariable=population,
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')

# input
Label(
    innerWindow,
    text="\n\n\nSet a custom IP Address:",
    font=(
        "Helvetica",
        14),
    anchor='w',
    wraplength=420).pack(
    fill='both')
customIP = tk.Entry(innerWindow, width=300)
customIP.insert(0, str(specificIP))
customIP.configure(state='disabled')
customIP.bind('<Button-1>', lambda e: placeholder(e, customIP))
customIP.pack()

# buttons
submit = Button(
    innerWindow,
    text="Submit",
    width=7,
    command=getCustomInformation)
submit.pack(side=tk.RIGHT)
clear = Button(innerWindow, text="Clear", width=7, command=clearText)
clear.pack(side=tk.RIGHT)
window.mainloop()
