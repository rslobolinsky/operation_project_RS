from config import DATA_TEST, DATA_TEST_LIST
from src.Operations import Operation


def test_get_operations_list():
    assert Operation().get_operations_list(DATA_TEST) == [1, 2, 3]


def test_clean_operations_list():
    operations = Operation()
    operations.get_operations_list(DATA_TEST)
    assert Operation().clean_operations_list([{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
        {'state': 'EXECUTED'}]
    assert Operation().clean_operations_list([{'state': 'EXECUTED'}, {}, {'state': 'CANCELED'}]) == [
        {'state': 'EXECUTED'}]
    assert len(operations.list_operation) == 3


def test_sort_list():
    assert Operation().sort_list([{'date': '2018-01-21T01:10:28.317704'}, {'date': '2018-12-18T17:07:09.800800'},
                                  {'date': '2019-12-08T22:46:21.935582'}]) == [
               {'date': '2019-12-08T22:46:21.935582'},
               {'date': '2018-12-18T17:07:09.800800'},
               {'date': '2018-01-21T01:10:28.317704'}]


def test_print_first_line():
    assert Operation().print_first_line("2019-12-08T22:46:21.935582", "Открытие вклада") == "08.12.2019 Открытие вклада"


def test_hide_card_info():
    assert Operation().hide_card_info("Visa Gold 7305799447374042") == "Visa Gold 7305 79** **** 4042"
    assert Operation().hide_card_info("Счет 96292138399386853355") == "Счет **3355"