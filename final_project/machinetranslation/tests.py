from translator import french_to_english
from translator import english_to_french
import unittest

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')
        
class TestfrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')

unittest.main()
