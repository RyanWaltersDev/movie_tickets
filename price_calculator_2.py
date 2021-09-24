class PriceCalculator:
    '''Calculate ticket price.'''

    def __init__(self, age=0, ticket=0, tickets=[]):
        '''Initialize attributes.'''
        self.age = age
        self.ticket = ticket
        self.tickets = tickets

    def younger_than_3(self, age, ticket=0):
        '''Print message and add no price.'''
        return (ticket, f"Your {age} year old child gets free admission!")

    def ages_3_to_12(self, age, ticket=0):
        '''Return ticket price and message for ages 3 to 12.'''
        ticket = 10
        return (ticket, f"The ticket price for a {age} year old is ${ticket}!")

    def ages_13_to_64(self, age, ticket=0):
        '''Return ticket price and message for ages 13 to 64.'''
        ticket = 15
        return(ticket, f"The ticket price for {age} year olds is ${ticket}!")

    def ages_65_and_older(self, age, ticket=0):
        '''Return ticket price and message for ages 65 and up.'''
        ticket = 12
        return(ticket, f"The ticket price for senior citizens is ${ticket}!")

    def veteran(self, age, ticket=0):
        '''Return ticket price and message for veterans'''
        ticket = 8
        return(ticket, 
            f"Thank you for your service. Your ticket price is ${ticket}!")

    def int_input_logic(self, age, tickets=[]):
        '''Return function based on age input and append ticket list.'''
        age = int(age)
        if age < 3:
            return self.younger_than_3(age)
        elif age >= 3 and age <= 12:
            result = self.ages_3_to_12(age)
            tickets.append(result[0])
            return tickets, result[0], result[1]
        elif age > 12 and age < 65:
            result = self.ages_13_to_64(age)
            tickets.append(result[0])
            return tickets, result[0], result[1]
        elif age >= 65 and age <=120:
            result = self.ages_65_and_older(age)
            tickets.append(result[0])
            return tickets, result[0], result[1]
        else:
            return ([], 0, "Please enter a valid age.")

    def string_input_logic(self, age, tickets=[]):
        '''Veteran and invalid response input logic.'''
        if age.title() == 'Veteran':
            result = self.veteran(age)
            tickets.append(result[0])
            return tickets, result[0], result[1]
        else:
            return ([], 0, "Please enter a valid response.")


    #def while_loop(self, age):


