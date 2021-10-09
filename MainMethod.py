#importing get from requests module for API calls
from requests import get
loc = get('https://ipapi.co/json/') #calling the api
ip = loc.json() #transforing it to json format to print it in the terminal
while (True) :#Loop will continue until the user chooses 'n' or to stop the program
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
    #condition on what to display
    if choice == '1':
        print("Your location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
    elif choice == '2':
        print("Your ip address is " + ip['ip'])
    elif choice == '3':
        print("Your internet service provider is " + ip['org'])
    elif choice == '4':
        print('Your country\'s currency is ' + ip['currency_name'])
    elif choice == '5':
        print('Your country\'s languages is ' + ip['languages'])
    elif choice == '6':
        print("Your autonomous system number is " + ip['asn'])
    elif choice == '7':
        print("Your country\'s Timezone is " + ip['timezone'])
    elif choice == '8':
        print("Your zip code is "+ ip['postal'])
    elif choice == '9':
        print("Your country\'s capital is " + ip['country_capital'])
    elif choice =='10':
        print("Your country\'s population is {}" .format(ip['country_population']))
    elif choice =='11':
        print("Your location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['country_name'])
        print("Your ip address is " + ip['ip'])
        print("Your internet service provider is " + ip['org'])
        print('Your country\'s currency is ' + ip['currency_name'])
        print('Your country\'s languages is ' + ip['languages'])
        print("Your autonomous system number is " + ip['asn'])
        print("Your country\'s Timezone is " + ip['timezone'])
        print("Your zip code is "+ ip['postal'])
        print("Your country\'s capital is " + ip['country_capital'])
        print("Your country\'s population is {}" .format(ip['country_population']))


    #Condition to end the program if the user enters "n" or "N"
    end = input("\nDo you want to continue? (Y/N)")
    if (end.lower() == "n"):
        print("""\n\t==========================================
        \tThis program was made by: \n
        \t   Marc Ricson Ricafort, \n
        \t     Stanley Orong III, \n
        \t   and Cyril Ken Verdad \n
        \t        From 4-ITG \n
        ==========================================""")
        break
    else:
        continue