from exercises.data_structures.HashTable import *
from ..utils.test_utils import *

class HashTableTest:
    def __init__(self):
        self.test_configs = [
            ["test_constructor", self.test_constructor],
            ["test_get_set_value", self.test_get_set_value],
            ["test_keys", self.test_keys]
        ]

    def run_all_tests(self):
        run_all_tests(self.test_configs)

    def initialize_test_hash_table(self):
        return HashTable()

    def test_constructor(self):
        ht = self.initialize_test_hash_table()
        return len(ht.data_map) == 7

    def test_get_set_value(self):
        ht = self.initialize_test_hash_table()

        result1 = ht.get_value("key1") == None
        ht.set_item("key1", 4)
        result2 = ht.get_value("key1") == 4
        return result1 and result2

    def test_keys(self):
        ht = HashTable()
        ht.set_item("key1", 21)
        ht.set_item("key2", 23)
        ht.set_item("key3", 12)
        ht.set_item("key1", 40)
        return sorted(ht.keys()) == ["key1", "key1", "key2", "key3"]