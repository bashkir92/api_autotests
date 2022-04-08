from clients.api_helper import ApiHousehold
from config import Config
from checker.general import Checker
from helpers.shkoda_helps import ShkodaHelps

class Application:
    def __init__(self):
        self.api = ApiHousehold()
        self.configs = Config()
        self.checker = Checker()
        self.helper = ShkodaHelps()
