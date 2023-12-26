from Operations import Operation
from config import DATA


def main():
    operations = Operation()
    operations.get_operations_list(DATA)
    operations.clean_operations_list(operations.list_operation)
    operations.sort_list(operations.list_operation)
    print(operations.get_last_info())




if __name__ == "__main__":
    main()

