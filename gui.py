from tkinter import *
#importing get from requests module for API calls
from requests import get
loc = get('https://ipapi.co/json/') #Fetching data from the api
ip = loc.json() #Formatting to json format to print it in the terminal

#main 
window = Tk()
window.title('IPGetR')
var = StringVar() #message textvariable
choices = StringVar()

#funtions
def click(): #onclick function
    enteredtext = textin.get()
    mylabel = Message(window, text = ' ')
    
    if enteredtext == '1':
        mylabel = Label(window, text = "\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
    elif enteredtext == '2':
        mylabel = Label(window, text = "\nYour ip address is " + ip['ip'])
    elif enteredtext == '3':
        mylabel = Label(window, text = "\nYour internet service provider is " + ip['org'])
    elif enteredtext == '4':
        mylabel = Label(window, text = '\nYour country\'s currency is ' + ip['currency_name'])
    elif enteredtext == '5':
        mylabel = Label(window, text = '\nYour country\'s languages is ' + ip['languages'])
    elif enteredtext == '6':
        mylabel = Label(window, text = "\nYour autonomous system number is " + ip['asn'])
    elif enteredtext == '7':
        mylabel = Label(window, text = "\nYour country\'s Timezone is " + ip['timezone'])
    elif enteredtext == '8':
        mylabel = Label(window, text = "\nYour zip code is "+ ip['postal'])
    elif enteredtext == '9':
        mylabel = Label(window, text = "\nYour country\'s capital is " + ip['country_capital'])
    elif enteredtext =='10':
        mylabel = Label(window, text = "\nYour country\'s population is {}" .format(ip['country_population']))
    elif enteredtext =='11':
        mylabel = Message(window, text = "\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name']
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
        mylabel = Label(window, text = "\n================Please enter only a number from 1 to 11.================")
        
    mylabel.pack()

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
textin = Entry(window, width= 10)
textin.pack()

#button 
submit = Button(window, text= "submit", width = 7 , command = click)
submit.pack()

window.mainloop()