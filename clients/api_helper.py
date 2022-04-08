from clients.orpon_id import ApiOrponId
from checker.general import Checker
from clients.shkoda import ApiShkoda
from clients.building_id import ApiBuildingId
from clients.codes import ApiCodes

class ApiHousehold:
    def __init__(self):
        self.orpon_id = ApiOrponId()
        self.checker = Checker()
        self.shkoda = ApiShkoda()
        self.building_id = ApiBuildingId()
        self.codes = ApiCodes()