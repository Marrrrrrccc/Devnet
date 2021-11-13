from tkinter import *
from tkinter import messagebox
#importing get from requests module for API calls
from requests import get
loc = get('https://ipapi.co/json/') #Fetching data from the api
ip = loc.json() #Formatting to json format to print it in the terminal

#main 
window = Tk()
window.title('IPGetR')
var = StringVar() #message textvariable
choices = StringVar()
window.resizable(0,0) #Sets the window to unresizable
window.geometry('550x600') #Adds a fixed width and height

#funtions
def click(): #onclick function
    enteredtext = textin.get()
    enteredtext1 = ipAddress.get()
    # if enteredtext1 is not empty then use it in the api call
    # error to be fixed
    # nakukuha naman ip address
    #pero may error
    # if enteredtext1:
    #     url = 'https://ipapi.co/' + enteredtext1 + '/json/'
    #     loc = get(url)
    #     ip1=loc.json()
    #     #print all the necessary data from the api call
    #     var.set(ip1['region'])
    #                       # text="\nYour location is  " + ip1['city'] + ", " + ip1['region'] + ", " + ip1['country_name']
    #                       #      + "\nYour ip address is " + ip1['ip']
    #                       #      + "\nYour internet service provider is " + ip1['org']
    #                       #      + '\nYour country\'s currency is ' + ip1['currency_name']
    #                       #      + '\nYour country\'s languages is ' + ip1['languages']
    #                       #      + "\nYour autonomous system number is " + ip1['asn']
    #                       #      + "\nYour country\'s Timezone is " + ip1['timezone']
    #                       #      + "\nYour zip code is " + ip1['postal']
    #                       #      + "\nYour country\'s capital is " + ip1['country_capital']
    #                       #      + "\nYour country\'s population is {}".format(ip1['country_population']))
    if enteredtext == '1':
        messagebox.showinfo("IPGetR", "\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
    elif enteredtext == '2':
        messagebox.showinfo("IPGetR", "\nYour ip address is " + ip['ip'])
    elif enteredtext == '3':
        messagebox.showinfo("IPGetR", "\nYour internet service provider is " + ip['org'])
    elif enteredtext == '4':
        messagebox.showinfo("IPGetR", '\nYour country\'s currency is ' + ip['currency_name'])
    elif enteredtext == '5':
        messagebox.showinfo("IPGetR", '\nYour country\'s languages is ' + ip['languages'])
    elif enteredtext == '6':
        messagebox.showinfo("IPGetR", "\nYour autonomous system number is " + ip['asn'])
    elif enteredtext == '7':
        messagebox.showinfo("IPGetR", "\nYour country\'s Timezone is " + ip['timezone'])
    elif enteredtext == '8':
        messagebox.showinfo("IPGetR", "\nYour zip code is "+ ip['postal'])
    elif enteredtext == '9':
        messagebox.showinfo("IPGetR", "\nYour country\'s capital is " + ip['country_capital'])
    elif enteredtext =='10':
        messagebox.showinfo("IPGetR", "\nYour country\'s population is {}" .format(ip['country_population']))
    elif enteredtext =='11':
        messagebox.showinfo("IPGetR",  "\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name']
            +"\nYour ip address is " + ip['ip']
            +"\nYour internet service provider is " + ip['org']
            +'\nYour country\'s currency is ' + ip['currency_name']
            +'\nYour country\'s languages is ' + ip['languages']
            +"\nYour autonomous system number is " + ip['asn']
            +"\nYour country\'s Timezone is " + ip['timezone']
            +"\nYour zip code is "+ ip['postal']
            +"\nYour country\'s capital is " + ip['country_capital']
            +"\nYour country\'s population is {}" .format(ip['country_population']))
    else: 
        messagebox.showerror('IPGetR',"=Please enter only a number from 1 to 11.")
        

def placeholder(event,text):
    text.configure(state='normal')
    text.delete('0', END)
#label/ message (static)
Message1 = Message(window, textvariable = var, width = 1000)
Message1.pack()
Message2 = Message(window, textvariable = choices,  width= 1000)
Message2.pack()

var.set("""
        |   WELCOME TO IPGetR   |
        |THE PROGRAM WHERE YOU CAN GET INFORMATION FROM YOUR IP |
        """)

choices.set("\nWhat do you want to display? \n"
                   "1. Current Location \n"
                   "2. Public Ip Address \n"
                   "3. Internet Service Provider \n"
                   "4. Currency\n"
                   "5. Languages\n"
                   "6. Autonomous system number\n"
                   "7. Timezone\n"
                   "8. Zip code\n"
                   "9. Country capital\n"
                   "10. Country Population\n"
                   "11. Display all of the above\n")
#input
textin = Entry(window, width= 30)
textin.insert(0, "Enter a number from 1 to 11")
textin.configure(state='disabled')
textin.bind('<Button-1>', lambda e: placeholder(e,textin))
textin.pack()

#placeholder
ipAddress = Entry(window, width= 30)
ipAddress.insert(0, "Enter your ip address")
ipAddress.configure(state='disabled')
ipAddress.bind('<Button-1>', lambda e: placeholder(e,ipAddress))
ipAddress.pack()

#button 
submit = Button(window, text= "submit", width = 7 , command = click)
submit.pack()

window.mainloop()
