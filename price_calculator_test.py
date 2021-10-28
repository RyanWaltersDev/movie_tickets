import unittest
from unittest.mock import patch
#from price_calculator import PriceCalculator
from price_calculator_2 import PriceCalculator

class PriceCalculatorTest(unittest.TestCase):
    '''Make sure our price calculator works'''

    def test_younger_than_3(self):
        '''Check to make sure that function prints correctly.'''
        instance = PriceCalculator()
        customer = instance.younger_than_3(2)
        self.assertEqual(customer, (0, '\nYour 2 year old child '
            'gets free admission!'))

    def test_ages_3_to_12(self):
        '''Check funtion formula and return message.'''
        instance = PriceCalculator()
        customer = instance.ages_3_to_12(12)
        self.assertEqual(customer, (10, 
            "\nThe ticket price for a 12 year old is $10!"))


    def test_ages_13_to_64(self):
        '''Check function formula and return message.'''
        instance = PriceCalculator()
        customer = instance.ages_13_to_64(25)
        self.assertEqual(customer, (15, 
            "\nThe ticket price for 25 year olds is $15!"))

    def test_ages_65_and_older(self):
        '''Check function formula and return message.'''
        instance = PriceCalculator()
        customer = instance.ages_65_and_older(76)
        self.assertEqual(customer, (12,
            "\nThe ticket price for senior citizens is $12!"))

    def test_veteran(self):
        '''Check function formula and return message.'''
        instance = PriceCalculator()
        customer = instance.veteran('veteran')
        self.assertEqual(customer, (8, 
            "\nThank you for your service. Your ticket price is $8!"))

    def test_int_input_logic(self):
        '''Check tuple return of function.'''
        instance = PriceCalculator()
        ticket, string = instance.int_input_logic(12)
        
        self.assertEqual(ticket, 10)
        self.assertEqual(string, "\nThe ticket price for a 12 year old is $10!")

    def test_vet_string_input_logic(self):
        '''Check tuple return of function.'''
        instance = PriceCalculator()
        ticket, string = instance.string_input_logic('veteran')
        
        self.assertEqual(ticket, 8)
        self.assertEqual(string, 
            "\nThank you for your service. Your ticket price is $8!")

    def test_invalid_int_input_logic(self):
        '''Check tuple when invalid integer entered.'''
        instance = PriceCalculator()
        response = instance.int_input_logic(500)
        self.assertEqual(response, (0, "\nPlease enter a valid age."))

    def test_invalid_string_input_logic(self):
        '''Check tuple when invalid string entered.'''
        instance = PriceCalculator()
        response = instance.string_input_logic('blah')
        self.assertEqual(response, (0, "\nPlease enter a valid response."))

    @patch('price_calculator_2.input', return_value='88')
    def test_user_input(self, mock_input):
        '''Check to make sure function returns user input.'''
        instance = PriceCalculator()
        response = instance.user_input()
        self.assertEqual(response, '88')

    def test_ticket_totaler_single_value(self):
        '''Check ticket totaler functionality when a single value entered.'''
        instance = PriceCalculator()
        response = instance.ticket_totaler(10)
        self.assertEqual(response, 10.7)

    #def test_ticket_totaler_multiple_value(self):
        '''Check ticket totaler functionality when multiple values entered.'''
        #instance = PriceCalculator()
        #response = instance.ticket_totaler(10)
        #response += instance.ticket_totaler(8)
        #response += instance.ticket_totaler(15)
        #self.assertEqual(response, 35.31)


if __name__ == '__main__':
    unittest.main()
