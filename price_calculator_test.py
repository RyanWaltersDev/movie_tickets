import unittest
#from price_calculator import PriceCalculator
from price_calculator_2 import PriceCalculator

class PriceCalculatorTest(unittest.TestCase):
    '''Make sure our price calculator works'''
    def setUp(self):
        self.instance = PriceCalculator()

    def tearDown(self):
        self.instance.ticket_list = []

    def test_younger_than_3(self):
        '''Check to make sure that function prints correctly.'''
        instance = PriceCalculator()
        customer = instance.younger_than_3(2)
        self.assertEqual(customer, (0, [], 'Your 2 year old child '
            'gets free admission!'))

    def test_ages_3_to_12(self):
        '''Check funtion formula and return message.'''
        instance = PriceCalculator()
        ticket, ticket_list, string = instance.input_logic(12)
        self.assertEqual(ticket, 10.7)
        self.assertEqual(ticket_list, [10.7])
        self.assertEqual(string, "The ticket price for a 12 year old is $10!")

    def test_ages_13_to_64(self):
        '''Check function formula and return message.'''
        instance = PriceCalculator()
        customer = instance.ages_13_to_64(25)
        self.assertEqual(customer, (16.05, [16.05], 
            "The ticket price for 25 year olds is $15!"))

    def test_ages_65_and_older(self):
        '''Check function formula and return message.'''
        instance = PriceCalculator()
        customer = instance.ages_65_and_older(76)
        self.assertEqual(customer, (12.84, [12.84],
            "The ticket price for senior citizens is $12!"))

    def test_input_logic(self):
        instance = PriceCalculator()
        ticket, ticket_list, string = instance.input_logic(12)
        self.assertEqual(ticket, 10.7)
        self.assertEqual(ticket_list, [10.7])
        self.assertEqual(string, "The ticket price for a 12 year old is $10!")

if __name__ == '__main__':
    unittest.main()
