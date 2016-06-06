import unittest
import four

class TestGreeter(unittest.TestCase):
    def test_with_empty_string(self):
        self.assertEqual(four.greeter(""), 'Hello, Mr Nobody!')

    def test_with_my_name(self):
        self.assertEqual(four.greeter("Slim Shady"), 'Hello, Slim Shady!')
    
if __name__ == '__main__':
    unittest.main()