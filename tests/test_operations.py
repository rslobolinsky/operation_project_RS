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