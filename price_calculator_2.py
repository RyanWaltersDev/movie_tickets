class PriceCalculator:
    '''
    Calculate ticket price based on user input.
    Call the while_loop method to run program.
    '''

    def __init__(self, age=0, ticket=0, tickets=[]):
        '''Initialize attributes.'''
        self.age = age
        self.ticket = ticket
        self.tickets = tickets

    def younger_than_3(self, age, ticket=0):
        '''Print message and add no price.'''
        return (ticket, f"\nYour {age} year old child gets free admission!")

    def ages_3_to_12(self, age, ticket=0):
        '''Return ticket price and message for ages 3 to 12.'''
        ticket = 10
        return (ticket, f"\nThe ticket price for a {age} year old is ${ticket}!")

    def ages_13_to_64(self, age, ticket=0):
        '''Return ticket price and message for ages 13 to 64.'''
        ticket = 15
        return(ticket, f"\nThe ticket price for {age} year olds is ${ticket}!")

    def ages_65_and_older(self, age, ticket=0):
        '''Return ticket price and message for ages 65 and up.'''
        ticket = 12
        return(ticket, f"\nThe ticket price for senior citizens is ${ticket}!")

    def veteran(self, age, ticket=0):
        '''Return ticket price and message for veterans'''
        ticket = 8
        return(ticket, 
            f"\nThank you for your service. Your ticket price is ${ticket}!")

    def int_input_logic(self, age):
        '''Return function based on age input and append ticket list.'''
        age = int(age)
        if age < 3:
            return self.younger_than_3(age)
        elif age >= 3 and age <= 12:
            result = self.ages_3_to_12(age)

            return result[0], result[1]
        elif age > 12 and age < 65:
            result = self.ages_13_to_64(age)
            
            return result[0], result[1]
        elif age >= 65 and age <=120:
            result = self.ages_65_and_older(age)
            
            return result[0], result[1]
        else:
            return (0, "\nPlease enter a valid age.")

    def string_input_logic(self, age):
        '''Veteran and invalid response input logic.'''
        if age.title() == 'Veteran':
            result = self.veteran(age)

            return result[0], result[1]
        else:
            return (0, "\nPlease enter a valid response.")

    def full_input_logic(self, user_input):
        '''Int and string input logic together.'''
        if user_input.isnumeric() == True:
            ticket, str = self.int_input_logic(user_input)
        else:
            ticket, str = self.string_input_logic(user_input)
        return ticket, str


    def user_input(self):
        '''Prompt user input and assign to variable.'''
        prompt = "\n\nThank you for choosing Runway Theaters!"
        prompt += "\n(Service members receive discounted prices! "
        prompt +="Enter 'veteran' to apply discount.)"
        prompt += "\n(If you are finished, please enter 'quit')"
        prompt += "\nEnter the age of the person that this ticket is for: "
        user_input = input(prompt)
        return user_input

    def ticket_totaler(self, ticket, tickets=[]):
        '''Calculates the total cost of tickets.'''
        tickets.append(ticket)
        total = sum(tickets)
        tax = total * 0.07 #Sales tax
        total += tax
        return total


    def while_loop(self):
        '''While loop that contains input logic.'''
        active = True
        while active:
            user_input = self.user_input()
            if user_input.title() == 'Quit':
                print("\n\nThank you for choosing Runway Theaters!")
                break
            else:
                ticket, str = self.full_input_logic(user_input)
                print(str)
                if ticket == 0:
                    continue
            
            total = self.ticket_totaler(ticket)
            print(f"Your current total is {total:.2f}.")

            more_ticket = input("Would you like to buy more tickets? [Y/N] ")
            if more_ticket.title() == 'Y' or more_ticket.title() == 'Yes':
                continue
            else:
                print(f"\n\nThank you for choosing Runway Theaters! "
                "Enjoy the movie!")
                active = False

#instance = PriceCalculator()
#instance.while_loop()