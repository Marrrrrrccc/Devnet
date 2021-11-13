from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label
#importing get from requests module for API calls
from requests import get

#functions
def getInformation(): #onclick function
    loc = get('https://ipapi.co/json/') #Fetching data from the api
    ip = loc.json() #Formatting to json format

    #referencing global variables
    global currentLoc
    global currentLoc
    global publicIP
    global serviceProvider
    global currency
    global languages
    global asn
    global timezone
    global zipCode
    global capital
    global population

    #setting variable information
    currentLoc = ip['city'] + ", " + ip['region'] + ", " + ip['country_name']
    publicIP = ip['ip']
    serviceProvider = ip['org']
    currency = ip['currency_name']
    languages = ip['languages']
    asn = ip['asn']
    timezone = ip['timezone']
    zipCode = ip['postal']
    capital = ip['country_capital']
    population = ip['country_population']
        


#main 
window = Tk()
window.title('IPGetR')
header = StringVar() #message textvariable
choices = StringVar()
window.resizable(0,0) #Sets the window to unresizable
window.geometry('570x600') #Adds a fixed width and height
innerWindow= Frame(window, relief= 'sunken') #Frame used to add virtual padding between window and text
innerWindow.pack(fill= BOTH, expand= True, padx= 75, pady=20)

#variables
currentLoc = ""
publicIP = ""
serviceProvider = ""
currency = ""
languages = ""
asn = ""
timezone = ""
zipCode = ""
capital = ""
population = ""

#Method to get initial information
getInformation()

#label/ message (static)
#Title
Label(innerWindow, text = "Welcome to IPGetR", font = ("Helvetica bold", 25)).pack()
Label(innerWindow, text = "The program where you can get information from your IP!  ", font = ("Helvetica", 14)).pack()
Label(innerWindow, text='\n\nYour Information', font=("Helvetica bold", 14), anchor='w').pack(fill='both')

#Content
Label(innerWindow, text='Current Location: ' +  str(currentLoc), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Public IP Address: ' + str(publicIP), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Internet Service Provider (ISP): ' + str(serviceProvider), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Currency: ' + str(currency), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Languages: ' + str(languages), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Autonomous System Number: ' + str(asn), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Timezone: ' + str(timezone), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text='Zip Code: ' + str(zipCode), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text="Country's Capital: " + str(capital), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')
Label(innerWindow, text="Countery's Population: " + str(population), font=("Helvetica", 14), anchor='w', wraplength=420).pack(fill='both')

# #input
# textin = Entry(window, width= 30)
# textin.insert(0, "Enter a number from 1 to 11")
# textin.configure(state='disabled')
# textin.bind('<Button-1>', lambda e: placeholder(e,textin))
# textin.pack()
# choices.set("\nWhat do you want to display? \n"
#                    "1. Current Location \n"
#                    "2. Public Ip Address \n"
#                    "3. Internet Service Provider \n"
#                    "4. Currency\n"
#                    "5. Languages\n"
#                    "6. Autonomous system number\n"
#                    "7. Timezone\n"
#                    "8. Zip code\n"
#                    "9. Country capital\n"
#                    "10. Country Population\n"
#                    "11. Display all of the above\n")
# #placeholder
# ipAddress = Entry(window, width= 30)
# ipAddress.insert(0, "Enter your ip address")
# ipAddress.configure(state='disabled')
# ipAddress.bind('<Button-1>', lambda e: placeholder(e,ipAddress))
# ipAddress.pack()

#button 
# submit = Button(window, text= "submit", width = 7 , command = click)
# submit.pack()

window.mainloop()
