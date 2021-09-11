class PriceCalculator():
    '''Calculate ticket price based on user input'''

    def __init__(self, age):
        '''Initalize attributes'''
        self.age = age
        ticket = 0
        ticket_list = []

    def input(self, age):
        if age.isnumeric == True:
            def integer_input(self, age):
                age = int(age)
                ticket = 0
                ticket_list = []
                # younger than 3
                if age < 3:
                    print(f"\n\tYour {age} year old child gets free admission!")
                # ages 3 to 12
                elif age >= 3 and age <= 12:
                    print(f"\tThe ticket price for a {age} year old is $10!")
                    ticket += 10
                    ticket += ticket * 0.07
                    ticket_list.append(ticket)
                # ages 12 to 64
                elif age > 12 and age < 65:
                    print(f"\tThe ticket price for {age} year olds is $15!")
                    ticket += 15
                    ticket += ticket * 0.07
                    ticket_list.append(ticket)
                # 65 and up
                elif age >= 65 and age < 120:
                    print(f"\tThe price for our senior citizens is $12!")
                    ticket += 12
                    ticket += ticket * 0.07
                    ticket_list.append(ticket)
                # Invalid age
                else:
                    print("\tPlease enter a valid age.")
                return ticket
        else:
            def string_input(self, age):
                # quit break
                if age.title() == 'Quit' or age.title() == "'Quit'":
                    break
                # veteran pricing
                elif age.title() == 'Veteran' or age.title() == "'Veteran'":
                    print(f"\tThank you for your service. Your ticket price is $8!")
                    ticket += 8
                    ticket += ticket * 0.07
                    ticket_list.append(ticket)
                # invalid response
                else:
                    print("\tPlease enter a valid response.")
                    continue
