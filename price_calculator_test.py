import unittest
#from price_calculator import PriceCalculator
from price_calculator_2 import PriceCalculator

class PriceCalculatorTest(unittest.TestCase):
    '''Make sure our price calculator works'''

    def test_younger_than_3(self):
        '''Check to make sure that function prints correctly.'''
        age = PriceCalculator(2)
        customer = age.younger_than_3(2)
        self.assertEqual(customer, 'Your 2 year old child '
            'gets free admission!')

    def test_ages_3_to_12(self):
        '''Check funtion formula and return message.'''
        age = PriceCalculator(5)
        customer = age.ages_3_to_12(4)
        self.assertEqual(customer, (10.7, [10.7], 
            "The ticket price for a 5 year old is $10!"))

    def test_ages_13_to_64(self):
        '''Check function formula and return message.'''
        age = PriceCalculator(25)
        customer = age.ages_13_to_64(25)
        self.assertEqual(customer, (16.05, [16.05], 
            "The ticket price for 25 year olds is $15!"))

    def test_ages_65_and_older(self):
        '''Check function formula and return message.'''
        age = PriceCalculator(76)
        customer = age.ages_65_and_older(76)
        self.assertEqual(customer, (12.84, [12.84],
            "The ticket price for senior citizens is $12!"))


if __name__ == '__main__':
    unittest.main()
