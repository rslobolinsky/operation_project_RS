import json
from datetime import datetime as date

class Operation:
    def __init__(self):
        self.list_operation = []

    def __repr__(self):
        return (f"Return file with information\n"
                f"about users operations:\n"
                f"{self.list_operations}\n")

    def get_operations_list(self, data_path):
        """
        Get list with operations from data file
        :param data_path: path to data file
        :return: list with user operations
        """
        with open(data_path, 'r', encoding='UTF-8') as data_file:
            self.list_operation = json.load(data_file)
        return self.list_operation

    def clean_operations_list(self, operations_list):
        """
        Clean None dict, info with CANCELED state and other artifacts
        :param operations_list: user's operations list
        :return: clean self.list_operations
        """
        new_list = []
        for info in operations_list:
            if info.get('state') == 'EXECUTED':
                new_list.append(info)
        self.list_operation = new_list
        return self.list_operation

    def sort_list(self, clean_operations_list):
        """
        Sort operations list
        :param clean_operations_list: clean operations list
        :return: self.list_operations fith 5 sort last operations
        """
        sorted(clean_operations_list, key=lambda dictionary: dictionary['date'], reverse=True)
        self.list_operation = sorted(clean_operations_list, key=lambda dictionary: dictionary['date'], reverse=True)
        self.list_operation = self.list_operation[:5]
        return self.list_operation

    def print_first_line(self, date_info, description):
        """
        Get formatted date and description
        :param date_info: info about date
        :param description: description
        :return: formatted date and description
        """
        date_class = date.fromisoformat(date_info)
        date_formatted = date_class.strftime("%d.%m.%Y")
        return f"{date_formatted} {description}"

    def hide_card_info(self, card_info):
        """
        Get hide info about card's number
        :param card_info: name and number card
        :return: name card and hide number
        """
        list_card_info = card_info.split()
        new_list = []
        for info in list_card_info:
            if 'счет' in card_info.lower() and info.isdigit():
                new_list.append(f'**{info[-4:]}')
            elif 'счет' not in card_info.lower() and info.isdigit():
                new_list.append(f'{info[:4]} {info[4:6]}** **** {info[-4:]}')
            else:
                new_list.append(info)
        return ' '.join(new_list)