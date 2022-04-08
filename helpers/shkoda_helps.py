import random
from random import choice

class ShkodaHelps:
    @staticmethod
    def generate_phone():
        phone = '8918' + str(random.randint(1111111, 9999999))
        return phone

    def generate_car_number(self):
        regions = ['123', '09', '01', '07']
        return 'А111АА ' + choice(regions)


    def generate_vin_code(self):
        vin_code = "JN1TBNT30U0124" + str(random.randint(111, 777))
        return vin_code