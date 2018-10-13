import csv
import json
import yaml

import re
import datetime

print('\n----------\nЗадание 1\n----------')

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']

def get_data(files):
    global main_data

    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    dict_of_match = {
        'Изготовитель системы:': os_prod_list,
        'Название ОС:': os_name_list,
        'Код продукта:': os_code_list,
        'Тип системы:': os_type_list
    }

    for file in files:
        with open(file, 'r') as file_r:
            read_file = file_r.readlines()

            for key, value in dict_of_match.items():
                for line in read_file:
                    result_match = re.match(key, line)

                    if result_match != None:
                        if key == 'Название ОС:':
                            pattern = re.compile(r'Windows\s*\S*')
                            result = pattern.findall(result_match.string)
                            value.append(result[0])
                        else:
                            pattern = re.compile(r'{}\s*\S*'.format(key))
                            result = pattern.findall(result_match.string)
                            value.append(result[0].split()[2])
                        break

    headers = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    i = 0
    while i < dict_of_match.__len__() - 1:
        row_data = []
        for key, value in dict_of_match.items():
            row_data.append(value[i])

        main_data.append(row_data)
        i = i + 1

    print(main_data)

def write_to_csv(main_data, writerow=True):

    with open('main_data.csv', 'w') as file_w:
        if writerow:
            writer = csv.writer(file_w)
            for row in main_data:
                writer.writerow(row)
        else:
            csv_writer = csv.writer(file_w, quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerows(main_data)

get_data(files)
write_to_csv(main_data)

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
                    print(f'key = {key}, value = {value}')
            elif method == 'loads':
                file_content = file_r.read()
                obj = json.loads(file_content)

                print(obj)

                for key, value in obj.items():
                    print(f'key = {key}, value = {value}')
            else:
                print(file_r.read())


JSON_operations = JSON_file_operations(
    dict_order('chair', 4, 5600, 'Pavel', datetime.datetime.now().strftime("%d-%m-%Y %H:%M")),
    file_name)

JSON_operations.write_order_to_json()
JSON_operations.read_order_from_json()

print('\n----------\nЗадание 3\n----------')

file_name = 'file.yaml'

def dict_for_yaml():

    value_1 = ['lesson', 2, 'csv', 'json', 'yaml']
    value_2 = 2018
    value_3 = {
        'RUB': '{} {}'.format(6556.06, b'\xe2\x82\xbd'.decode('utf-8')),
        'USD': '{} {}'.format(100, b'$'.decode('utf-8')),
        'EUR': '{} {}'.format(86.1513, b'\xe2\x82\xac'.decode('utf-8'))
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
        with open(self.file, 'w', encoding='utf8') as file_w:
            yaml.dump(self.dict, file_w, default_flow_style=False, allow_unicode=True)

    def read_dict_from_yaml(self):
        with open(self.file,'r', encoding='utf-8') as file_r:
            return yaml.load(file_r)


dict_before_w = dict_for_yaml()

YAML_operations = YAML_file_operations(dict_before_w, file_name)

YAML_operations.write_dict_to_yaml()
dict_after_w = YAML_operations.read_dict_from_yaml()
print(dict_after_w)

if dict_before_w == dict_after_w:
    result = 'равно'
else:
    result = 'не равно'

print(f'Содержание словарей до и после записи {result}')