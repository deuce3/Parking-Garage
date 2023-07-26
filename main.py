class ParkingGarage:
    user_input = " "
    park = " "

    # - tickets -> list
    # - parking_spaces -> list
    # - current_ticket -> dictionary
    def __init__(self, tickets, parking_spaces, current_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    # take_ticket()
    # - This should decrease the amount of tickets available by 1
    # - This should decrease the amount of parkingSpaces available by 1
    def take_ticket(self):
        self.tickets = self.tickets[:-1]
        self.parking_spaces = self.parking_spaces[:-1]

        print("\nTicket printed! Number of tickets remaining: ", len(self.tickets))
        print("Parking spot taken! Number of parking spots remaining: ", len(self.parking_spaces))

    # pay_for_parking()
    # - Display an input that waits for an amount from the user and store it in a variable
    # - If the payment variable is not empty then (meaning the ticket has been paid)
    #   -> display a message to the user that their ticket has been paid, and they have 15 minutes to leave
    #  -This should update the "currentTicket" dictionary key "paid" to True
    def pay_for_parking(self):
        while True:
            print("\nTickets are $1")
            self.user_input = input("Purchase a ticket: $")
            if self.user_input:
                if self.user_input == "1":
                    print("\nYour ticket has been purchased! You have 15 minutes to stay before you must leave.")
                    self.current_ticket["Paid"] = True
                    break
                else:
                    print("\nPlease purchase a ticket for exactly $1 or type 'leave' exit the garage.")
            else:
                print("\nI'm sorry, your response was not accepted. Please enter 1 to purchase a ticket.")

    # leave_garage()
    # - If the ticket has been paid, display a message of "Thank You, have a nice day"
    # - If the ticket has not been paid, display an input prompt for payment
    # - Once paid, display message "Thank you, have a nice day!"
    # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
    # - Update tickets list to increase by 1 (meaning add to the tickets list)
    def leave_garage(self):
        if self.current_ticket["Paid"]:
            self.tickets.append("Ticket")
            self.parking_spaces.append("Open")
            print("\nTime is up! Thank you, have a nice day.")
        else:
            self.pay_for_parking()

    def run(self):
        while True:
            park = input("Would you like to park in our garage? Yes/No ")
            if park.lower() == "yes":
                self.take_ticket()
                self.pay_for_parking()
                self.leave_garage()
                break
            else:
                print("No worries. Have a good day!")
                break


# Test Cases
test_list1 = ["Ticket", "Ticket", "Ticket"]
test_list2 = ["Open", "Open", "Open"]
test_dict1 = {"Paid": False}
garage = ParkingGarage(test_list1, test_list2, test_dict1)

if __name__ == '__main__':
    garage.run()
