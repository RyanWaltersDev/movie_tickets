class PriceCalculator:
    '''Calculate ticket price.'''

    def __init__(self, age=0, ticket=0, ticket_list=[]):
        '''Initialize attributes.'''
        self.age = age
        self.ticket = ticket
        self.ticket_list = ticket_list

    def younger_than_3(self, age, ticket=0, ticket_list=[]):
        '''Print message and add no price.'''
        return (ticket, ticket_list, 
            f"Your {age} year old child gets free admission!")

    def ages_3_to_12(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 3 to 12.'''
        ticket += 10
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return [ticket, ticket_list, 
            f"The ticket price for a {age} year old is $10!"]

    def ages_13_to_64(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 13 to 64.'''
        ticket += 15
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return(ticket, ticket_list,
            f"The ticket price for {age} year olds is $15!")

    def ages_65_and_older(self, age, ticket=0, ticket_list=[]):
        '''Return ticket price and message for ages 65 and up.'''
        ticket += 12
        ticket += ticket * 0.07
        ticket_list.append(ticket)
        return(ticket, ticket_list,
            f"The ticket price for senior citizens is $12!")

    def input_logic(self, age):
        '''Return function based on age input'''
        age = int(age)
        if age < 3:
            return self.younger_than_3(age)
        elif age >= 3 and age <= 12:
            return self.ages_3_to_12(age)
        elif age > 12 and age < 65:
            return self.ages_13_to_64(age)
        elif age >= 65 and age <=120:
            return self.ages_65_and_older(age)
        else:
            return (0, [], "Please enter a valid age.")

#instance = PriceCalculator()
#customer = instance.ages_3_to_12(12)
#print(customer)

#instance = PriceCalculator()
#a,b,c = instance.input_logic(12)
#print(a)
#print(b)
#print(c)