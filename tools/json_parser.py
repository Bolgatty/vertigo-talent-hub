'''
Author : Varsha Nizampure
project : Talent_Hunt
Date : 09/10/2020
program : Create a Json string format .
'''

import json


# create a class called JsonParser
class JsonParser:

    #Convert python objects into Json strings : Serialization
    def serialization(self, dict_data):
        print(dict_data)
        self.json_serstr = json.dumps(dict_data, sort_keys=True, indent=3)
        return self.json_serstr

    #Convert string into Json object - Deserialize python dict to json string
    def deserialization(self, json_string):
        # test_string = {"name": "Omkar Pathak", "email": "omkarpathak27@gmail.com", "designation": "Manager"}
        # data1 = json.dumps(test_string)
        data_deser = json.loads(json_string)
        return data_deser

    # def get_jd_json(self):

    # def get_vendor_json(self):