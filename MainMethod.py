#importing get from requests module for API calls
from requests import get

#version 1
loc = get('https://ipapi.co/json/') #Fetching data from the api
ip = loc.json() #Formatting to json format to print it in the terminal

#prints opening message
print("""\n\t=========================================================
        | \t\t    WELCOME TO IPGetR\t\t        |
        |THE PROGRAM WHERE YOU CAN GET INFORMATION FROM YOUR IP |
        =========================================================""")


while (True) : #Loop will continue until the user chooses 'n' or to stop the program
    choice = input("\nWhat do you want to display? \n"
                   "1. Current Location \n"
                   "2. Public Ip Address \n"
                   "3. Service Provider \n"
                   "4. Currency\n"
                   "5. Languages\n"
                   "6. autonomous system number\n"
                   "7. Timezone\n"
                   "8. Zip code\n"
                   "9. Country capital\n"
                   "10. Country Population\n"
                   "11. Display all of the above\n"
                   )
    #Condition on what to display depending on user input
    if choice == '1':
        print("\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
    elif choice == '2':
        print("\nYour ip address is " + ip['ip'])
    elif choice == '3':
        print("\nYour internet service provider is " + ip['org'])
    elif choice == '4':
        print('\nYour country\'s currency is ' + ip['currency_name'])
    elif choice == '5':
        print('\nYour country\'s languages is ' + ip['languages'])
    elif choice == '6':
        print("\nYour autonomous system number is " + ip['asn'])
    elif choice == '7':
        print("\nYour country\'s Timezone is " + ip['timezone'])
    elif choice == '8':
        print("\nYour zip code is "+ ip['postal'])
    elif choice == '9':
        print("\nYour country\'s capital is " + ip['country_capital'])
    elif choice =='10':
        print("\nYour country\'s population is {}" .format(ip['country_population']))
    elif choice =='11':
        print("\nYour location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
        print("Your ip address is " + ip['ip'])
        print("Your internet service provider is " + ip['org'])
        print('Your country\'s currency is ' + ip['currency_name'])
        print('Your country\'s languages is ' + ip['languages'])
        print("Your autonomous system number is " + ip['asn'])
        print("Your country\'s Timezone is " + ip['timezone'])
        print("Your zip code is "+ ip['postal'])
        print("Your country\'s capital is " + ip['country_capital'])
        print("Your country\'s population is {}" .format(ip['country_population']))
    else: 
        print("\n================Please enter only a number from 1 to 11.================")
        continue


    #Condition to end the program if the user enters "n" or "N"
    
    while (True):
        end = input("\nDo you want to display another? (Y/N)")
        if (end.lower() == "y"):
            print("\n==========================================")
            break
        elif (end.lower() == "n"):
            print("\nThank you for using our application.")
            print("""\n\t    ======================================
            |\t  This program was made by: \t |\t
            |\t     Marc Ricson Ricafort, \t |\t
            |\t       Stanley Orong III, \t |\t           
            |\t     and Cyril Ken Verdad \t |\t
            |\t          From 4-ITG \t\t |
            ======================================""")
            break
        else:
            print("\n================Please enter only Y or N================")
            continue

    #Condition to repeat program from the top
    if (end.lower() == "y"):
        continue
    else:
        break