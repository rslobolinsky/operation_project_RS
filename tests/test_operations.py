from config import DATA_TEST, DATA_TEST_LIST
from src.Operations import Operation


def test_get_operations_list():
    assert Operation().get_operations_list(DATA_TEST) == [1, 2, 3]