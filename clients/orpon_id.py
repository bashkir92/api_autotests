import requests
import copy
from config import Config

class ApiOrponId:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {'accept': 'application/json'}

    def get_buildings_by_orpon_id(self, id, token):
        api_method = '/api/v4/flatgramms/buildings/orpon_id/'
        url = self.url + api_method + str(id)

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response
