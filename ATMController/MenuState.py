from CashBin import CashBin
from DummyBankAPI import DummyBankAPI

#MenuState is a class that contains the methods used at various states in the ATM workflow
class MenuState:
    def __init__(self):
        self.state = 'Insert Card'
        self.card_id = 0
        self.pin = 0
        self.selected_account = 0
        self.account = 0
        self.check_pin_result = 0
        self.account_info = 0
        self.bank = DummyBankAPI()
        self.cash_bin = CashBin()

    #checks balance of currently selected account
    def check_balance(self):
        print(self.selected_account, 'Balance: $', self.bank.account_values[self.card_id][self.selected_account])

    #deposits entered amount into ATM cash box and currently selected account
    def make_deposit(self):
        amount = input('How munch money would you like to deposit?\n$')
        if amount.isnumeric():
            amount = int(amount)
            deposit_result = self.cash_bin.deposit(amount)
            if deposit_result==1:
                self.bank.change_balance(amount, self.pin, self.card_id, self.selected_account)
                print('$',amount, 'deposited into', self.selected_account)
            else:
                print(deposit_result)
        else:
            print('Invalid input, returning to menu')

    #withdraws entered amount from ATM cash box and currently selected account
    def make_withdrawal(self):
        amount = input('How much money would you like to withdraw?\n$')
        if amount.isnumeric():
            amount = int(amount)
            if amount <= self.bank.account_values[self.card_id][self.selected_account]:
                withdraw_result = self.cash_bin.withdraw(amount)
                if withdraw_result == 1:
                    self.bank.change_balance(-amount, self.pin, self.card_id, self.selected_account)
                    print('$', amount, 'withdrawn from', self.selected_account)
                else:
                    print(withdraw_result)
            else:
                print('Insufficient funds, withdrawal not made')
        else:
            print('Invalid input, returning to menu')

    #'reads' the card. Fixed value for testing
    def read_card(self):
        self.card_id = '1234567890'

    #Method called when ATM is in 'Insert Card' state
    def query_card(self):
        input('Please Insert Card and Press Enter to Continue')
        self.read_card()
        print('Card ID: ', self.card_id, ' detected')
        self.state = 'Enter Pin'

    # Method called when ATM is in 'Enter Pin' state
    def query_pin(self):
        self.pin = input('Please Enter PIN: ')
        while not self.pin.isnumeric():
            self.pin = input('Invalid input, please enter numeric pin: ')
        self.check_pin_result = self.bank.check_pin(self.pin,self.card_id)

        if self.check_pin_result==1:
            print('Successfully logged into account')
            self.state = 'Select Account'
        else:
            print(self.check_pin_result)

    # Method called when ATM is in 'Select Account' state
    def query_account(self):
        self.account_info = self.bank.get_accounts(self.pin, self.card_id)
        print('Accounts: ',)
        keys = {}
        i=1
        for key in self.account_info:
            print(i, ': ', key)
            keys.update({i:key})
            i+=1
        i = input('Please type selection number and press enter to select an account to access: ')
        if i.isnumeric():
            i=int(i)
            if i in keys:
                self.selected_account = keys[i]
                print(self.selected_account, ' Selected')
                self.state = 'Select Account Action'
            else:
                print('Option number', i, 'not available, please try again')
        else:
            print('Invalid input, returning to menu')

    # Method called when ATM is in 'Select Account Action' state
    def query_account_action(self):
        print('\n', self.selected_account, 'Options:')
        account_action = input('\n1: Check Balance\n2: Make a Deposit\n3: Make a Withdrawal\n4: Select a Different Account\n5: Log Out\n\nPlease select account action: ')
        print('\n')
        if account_action == '1':
            self.check_balance()
        elif account_action == '2':
            self.make_deposit()
        elif account_action == '3':
            self.make_withdrawal()
        elif account_action == '4':
            self.state = 'Select Account'
        elif account_action == '5':
            self.state = 'Insert Card'
            print('Logged Out\n')
        else:
            print('Invalid input, please try again')