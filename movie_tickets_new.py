#!/usr/bin/env python3
# RyanWaltersDev Jun 15 2021 -- TIY 7-5

# Initial prompt
prompt = "\n\nThank you for choosing Runway Theaters!"
prompt += "\n(Type 'veteran' to see our discount options for service members.)"
prompt += "\n(If you are finished, please enter 'quit')"
prompt += "\n\nEnter the age of the person that this ticket is for: "

# while loop
active = True
ticket_list = []
while active:
    age = input(prompt)
    ticket = 0

    # integer input
    if age.isnumeric() == True:
        age = int(age)
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

    # string input
    else:
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

    # calculate ticket total
    total = 0
    for tickets in range(0, len(ticket_list)):
        total = total + ticket_list[tickets]
    print(f"\nYour current total is ${total}.")
    
    # ask to continue
    more_ticket = input("Would you like to buy more tickets? [Y/N] ")
    if more_ticket.title() == 'Y' or more_ticket.title() == 'Yes':
        continue
    else:
        print(f"\n\nThank you for choosing Runway Theaters! Enjoy the movie!")
        active = False


# END OF PROGRAM
