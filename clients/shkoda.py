import requests
from config import Config

class ApiShkoda:
    def __init__(self):
        self.url_shkoda = Config.url_shkoda
        self.headers = {'accept': 'application/json'}
        self.headers["Content-Type"] = "application/json"

    def get_cars(self):
        api_method = '/api/cars/'
        url_shkoda = self.url_shkoda + api_method

        headers = {"Accept": "application/json"}
        headers["Content-Type"] = "application/json"

        response = requests.get(url_shkoda, headers=headers)
        return response

    def get_dealers(self):
        api_method = '/api/dealers/'
        url_shkoda = self.url_shkoda + api_method

        headers = {"Accept": "application/json"}
        headers["Content-Type"] = "application/json"

        response = requests.get(url_shkoda, headers=headers)
        return response

    def get_model_shkoda(self, model):
        api_method = '/api/cars/'
        url_shkoda = self.url_shkoda + api_method + model

        headers = {"Accept": "application/json"}
        headers["Content-Type"] = "application/json"

        response = requests.get(url_shkoda, headers=headers)
        return response

    def post_shkoda(self, dealer, car, first_name, patronymic, last_name, date, time, phone, email, car_number, vin):
        api_method = 'api/request'
        url_shkoda = self.url_shkoda + api_method

        req_dict = {
                "dealer": dealer,
                "car": car,
                "first_name": first_name,
                "patronymic": patronymic,
                "last_name": last_name,
                "date": date,
                "time": time,
                "phone": phone,
                "email": email,
                "car_number": car_number,
                "vin": vin
        }

        headers = {"Accept": "application/json"}
        headers["Content-Type"] = "application/json"

        response = requests.post(url_shkoda, headers=headers, json=req_dict)
        return response


    def get_city(self):
        api_method = '/api/cities/'
        url_shkoda = self.url_shkoda + api_method

        headers = {"Accept": "application/json"}
        headers["Content-Type"] = "application/json"

        response = requests.get(url_shkoda, headers=headers)
        return response