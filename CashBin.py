#Manages money in ATM. Limited capabilities included to allow testing of main ATM controller program.
class CashBin:
    def __init__(self):
        self.balance = 100

    #placeholder to physically dispense cash. Simply returns 1 to indicate success for now
    def dispense(self, dispense_amount):
        #Does hardware stuff
        return 1

    #attempts to dispense cash if enough in cash bin
    def withdraw(self, withdraw_amount):
        if self.balance>=withdraw_amount:
            self.dispense(withdraw_amount)
            self.balance -= withdraw_amount
            return 1
        failure_message ='Not enough cash in ATM. Only $' + str(self.balance) + ' left for withdrawal. Withdrawal canceled'
        return failure_message

    #counts and accepts cash deposits
    def deposit(self, deposit_amount):
        self.count_deposit(deposit_amount)
        self.balance += deposit_amount
        return 1

    #counts cash deposits
    def count_deposit(self, count_amount):
        return count_amount
