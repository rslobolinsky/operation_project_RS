import json


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