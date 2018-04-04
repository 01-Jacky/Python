import unittest

class Widget:
    def __init__(self, desc):
        self.description = desc

    def dispose(self):
        pass


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_widget_description(self):
        self.assertEqual(self.widget.description, 'The widget')

    def tearDown(self):
        self.widget.dispose()

if __name__ == '__main__':
    unittest.main()