class PriceCalculator():
    '''Calculate ticket price.'''

    def __init__(self, age):
        '''Initialize attributes.'''
        self.age = age

    def younger_than_3(self, age):
        '''Print message and add no price.'''
        return f"Your {self.age} year old child gets free admission!"


