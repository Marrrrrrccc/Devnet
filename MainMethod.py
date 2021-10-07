#need natin ng mga comments
from requests import get

loc = get('https://ipapi.co/json/')
ip = loc.json()
choice = input("What do you want to display?")

print("My location is " + ip['city'] + ", " + ip['region'] +", "+ ip['country_name'] )
print("My ip address is "+ ip['ip'])
print("My internet service provider is " + ip['org'])