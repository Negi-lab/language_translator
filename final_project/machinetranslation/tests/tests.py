'''assertEqual' & 'assertNotEqual' tests for the created functions
'''

#Suchit's Code starts:
import unittest

from machinetranslation.translator import english_french, french_english

#Test for the 'englishToFrench' function
class Test_English_to_French(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_french("Hello"), "Bonjo")


#Test for the 'frenchToEnglish' function
class Test_French_to_English(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_english("Bonjour"), "Hello")
        self.assertNotEqual(french_english("Bonjour"), "Helo")

unittest.main()
#Suchit's code ends
