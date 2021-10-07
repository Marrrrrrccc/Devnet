#importing get from requests module for API calls
from requests import get


while (True) :
    # loc = get('https://ipapi.co/json/')
    # print(loc.json())
    # ip = loc.json()
    choice = input("\nWhat do you want to display? \n1. Current Location \n2. Public Ip Address \n3. Service Provider \n")

    # print("My location is " + ip['city'] + ", " + ip['region'] +", "+ ip['country_name'] )
    # print("My ip address is "+ ip['ip'])
    # print("My internet service provider is " + ip['org'])

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