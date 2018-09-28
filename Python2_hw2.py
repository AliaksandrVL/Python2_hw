import csv
import json
import yaml

import datetime

print('\n----------\nЗадание 1\n----------')



print('\n----------\nЗадание 2\n----------')

file_name = 'orders.json'

def dict_order(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    return order

class JSON_file_operations:

    def __init__(self, order, file):
        self.order = order
        self.file = file

    def write_order_to_json(self):
        with open(self.file, 'w') as file_w:
            json.dump(self.order, file_w, indent=4)

    def read_order_from_json(self, method=''):
        with open(self.file, 'r') as file_r:
            if method == 'load':
                obj = json.load(file_r)

                print(obj)

                for key, value in obj.items():
                    print('key = {}, value = {}'.format(key, value))
            elif method == 'loads':
                file_content = file_r.read()
                obj = json.loads(file_content)

                print(obj)

                for key, value in obj.items():
                    print('key = {}, value = {}'.format(key, value))
            else:
                print(file_r.read())


JSON_operations = JSON_file_operations(
    dict_order('chair', 4, 5600, 'Pavel', datetime.datetime.now().strftime("%d-%m-%Y %H:%M")),
    file_name)

JSON_operations.write_order_to_json()
JSON_operations.read_order_from_json()

print('\n----------\nЗадание 3\n----------')

file_yaml = 'file.yaml'

def dict_for_yaml():

    value_1 = ['U+03E4', 'U+03E7']
    value_2 = 28
    value_3 = {
        'key_1': b'\U+0033\U+0038',
        'key_2': b'\U+0039\U+0031'
    }

    dict_yaml = {
        'key_1': value_1,
        'key_2': value_2,
        'key_3': value_3,
    }

    return dict_yaml

class YAML_file_operations:

    def __init__(self, dict, file):
        self.dict = dict
        self.file = file

    def write_dict_to_yaml(self):
        with open(self.file, 'w') as file_w:
            yaml.dump(self.dict, file_w, default_flow_style=False)

    def read_dict_from_yaml(self):
        pass