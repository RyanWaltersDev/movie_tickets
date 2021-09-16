class PriceCalculator():
    '''Calculate ticket price.'''

    def __init__(self, age, ticket=0, ticket_list=[]):
        '''Initialize attributes.'''
        self.age = age
        self.ticket = ticket
        self.ticket_list = ticket_list

    def younger_than_3(self, age):
        '''Print message and add no price.'''
        return f"Your {self.age} year old child gets free admission!"

    def ages_3_to_12(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 3 to 12.'''
        ticket += 10
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return (ticket, ticket_list, 
            f"The ticket price for a {self.age} year old is $10!")

    def ages_13_to_64(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 13 to 64.'''
        ticket += 15
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return(ticket, ticket_list,
            f"The ticket price for {self.age} year olds is $15!")

    def ages_65_and_older(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 65 and up.'''
        ticket += 12
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return(ticket, ticket_list,
            f"The ticket price for senior citizens is $12!")

