# Program to get information of a phone number
import time
import phonenumbers
from phonenumbers import timezone, geocoder, carrier 
  
# Parsing String to Phone number
phonenumber = phonenumbers.parse(input('Enter in your number with country code:'))
  
# Pass the parsed phone number in below function

timezone = timezone.time_zones_for_number(phonenumber)
  
# Checking the carrier of phonenumber
carrier = carrier.name_for_number(phonenumber, 'en')

# Checking the region of phonenumber
region = geocoder.description_for_number(phonenumber, 'en')

# Checking the possibility of phonenumber
possible = phonenumbers.is_possible_number(phonenumber)

time.sleep(3)
class Phone_Hunter_X:
  def __init__(self):
    print('[!]-------Fetching Details-------[!]')
    time.sleep(4)
    print('[*] Running local scan....')
    time.sleep(4)
    print('[*] {}'.format(phonenumber))
    time.sleep(3)
    print('[*] Timezone: {}'.format(timezone))
    time.sleep(3)
    print('[*] Carrier: {}'.format(carrier))
    time.sleep(4)
    print('[*] Region:{0}'.format(region))
    time.sleep(4)   
    print('[*] Valid/Possible: {0}'.format(possible))


# Invoking dunder __init__ using (). and also creating a class instance.
# Parentheses and instance is used to call __init__ due to which __init__ ends up getting excecuted.
hunter_x_instance = Phone_Hunter_X()
