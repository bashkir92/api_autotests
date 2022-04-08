import json
import jsonschema



class Checker:
    @staticmethod
    def validate_json(response, path_to_schema):
       path = 'C:/Users/Oleg.Bashkirov/Desktop/api_autotests_bashkirov' + '/' + path_to_schema
       with open(path) as file:
          schema = json.load(file)

       jsonschema.validate(response, schema)
       return True

    def validate_items(self, items_dict: list, path_to_schema: str):
        res_set = {True}
        for item in items_dict:
            res_set.add(self.validate_json(item, path_to_schema))
        return res_set