import unittest
#from price_calculator import PriceCalculator
from price_calculator_2 import PriceCalculator

class PriceCalculatorTest(unittest.TestCase):
    '''Make sure our price calculator works'''

    def test_younger_than_3(self):
        '''Check to make sure that function prints correctly'''
        age = PriceCalculator(2)
        child = age.younger_than_3(2)
        self.assertEqual(child, 'Your 2 year old child '
            'gets free admission!')

if __name__ == '__main__':
    unittest.main()
