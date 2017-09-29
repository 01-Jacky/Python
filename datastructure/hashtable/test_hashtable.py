import unittest
import hashtable

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.alphabet_map = hashtable.HashTable(27)
        for i in range(1, 26+1):
            self.alphabet_map.set(chr(ord('a')+i-1), i)

    def test_constructor(self):
        hashmap = hashtable.HashTable()          # hashmap constructors with some default fixed bin size > 1
        self.assertGreater(len(hashmap.bins), 1)

        hashmap = hashtable.HashTable(10)
        self.assertEqual(len(hashmap.bins), 10)

        hashmap = hashtable.HashTable(100)
        self.assertEqual(len(hashmap.bins), 100)

    def test_set(self):
        hashmap = hashtable.HashTable()
        hashmap.set('a', 1)
        self.assertEqual(hashmap.size, 1)
        hashmap.set('b', 2)
        self.assertEqual(hashmap.size, 2)
        hashmap.set('c', 'carrot')
        self.assertEqual(hashmap.size, 3)

        with self.assertRaises(TypeError):                  # Keys must be strings
            hashmap.set(4, "this should not get set")
        self.assertEqual(hashmap.size, 3)

    def test_set_update_value(selfs):
        pass

    def test_get(self):
        self.assertEqual(self.alphabet_map.get('c'), 3)
        self.assertEqual(self.alphabet_map.get('a'), 1)
        self.assertEqual(self.alphabet_map.get('b'), 2)
        self.assertEqual(self.alphabet_map.get('z'), 26)
        self.assertEqual(self.alphabet_map.get('I am not an existing key'), None)

    def test_delete(self):
        hashmap = hashtable.HashTable()
        hashmap.set('a', 1)
        hashmap.set('b', 2)
        hashmap.set('c', 3)

        self.assertEqual(hashmap.delete('c'), 3)
        self.assertEqual(hashmap.get('a'), 1)
        self.assertEqual(hashmap.get('b'), 2)
        self.assertEqual(hashmap.get('z'), None)

    def test_load(self):
        pass

    def test_set_get_delete_sequence(self):
        pass

if __name__ == '__main__':
    unittest.main()