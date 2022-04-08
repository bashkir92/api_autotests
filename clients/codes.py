import requests
import copy
from config import Config

class ApiCodes:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {'accept': 'application/json'}

    def delete_codes_by_id(self, id, token):
        api_method = '/api/v4/devices/codes/'
        url = self.url + api_method + str(id)

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = requests.delete(url, headers=headers)
        return response