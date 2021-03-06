import unittest
from work import anagramm

class TestWork(unittest.TestCase):
    
    def test_empty(self):
        self.assertTrue(anagramm('',''))
        
    def test_different_length_values(self):
        self.assertFalse(anagramm('','b'))
        
    def test_two_long_anagramms(self):
        self.assertTrue(anagramm('am','ma'))
    
    def test_two_long_anagramms2(self):
        self.assertTrue(anagramm('il', 'li'))
        
    def test_two_long_not_anagramms(self):
        self.assertFalse(anagramm('me','ki'))
        
    def test_three_long_anagramms(self):
        self.assertTrue(anagramm('meo','emo'))
    
    def test_three_long_anagramms2(self):
        self.assertTrue(anagramm('meo','eom'))
        
    def test_three_long_not_anagramms(self):
        self.assertFalse(anagramm('kai','akk'))
        
    def test_different_length_semi_anagramms(self):
        self.assertFalse(anagramm('kai','bika'))
    
    
if __name__ == '__main__':
    unittest.main()