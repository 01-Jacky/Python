import unittest
import hashtable
import math

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.alphabet_map = hashtable.HashTable(26)
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

        with self.assertRaises(TypeError):
            hashmap.set(4, "keys should be strings")
        self.assertEqual(hashmap.size, 3)

        with self.assertRaises(ValueError):
            self.alphabet_map.set('aa', "fixed sized map is full")
            self.assertEqual(hashmap.size, 26)

    def test_set_update_value(self):
        self.assertEqual(self.alphabet_map.get('a'), 1)
        self.alphabet_map.set('a','some new value')
        self.assertEqual(self.alphabet_map.get('a'), 'some new value')

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

    def test_set_get_delete_sequence(self):
        hashmap = hashtable.HashTable()
        hashmap.set('a', 1)
        hashmap.set('b', 2)
        self.assertEqual(hashmap.get('a'), 1)
        self.assertEqual(hashmap.delete('a'), 1)
        self.assertEqual(hashmap.delete('a'), None)

    def test_load(self):
        self.assertAlmostEqual(self.alphabet_map.load(), 1.0)
        with self.assertRaises(ValueError):
            self.alphabet_map.set('aa', "i'm too full")
        self.alphabet_map.delete('a')
        self.assertTrue(math.isclose(self.alphabet_map.load(), 25/26, rel_tol=1e-6))

        hashmap = hashtable.HashTable(10)
        hashmap.set('thing1', 1)
        self.assertAlmostEqual(hashmap.load(), 1/10)
        hashmap.set('thing2', 2)
        self.assertAlmostEqual(hashmap.load(), 2/10)
        hashmap.set('thing3', 3)
        self.assertAlmostEqual(hashmap.load(), 3/10)
        hashmap.delete('thing1')
        self.assertAlmostEqual(hashmap.load(), 2/10)
        hashmap.delete('thing2')
        self.assertAlmostEqual(hashmap.load(), 1/10)
        hashmap.delete('thing3')
        self.assertEqual(hashmap.load(), 0)


if __name__ == '__main__':
    unittest.main()