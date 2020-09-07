# dummy bank API class to allow testing of ATM controller. Single account with basic account methods.
class DummyBankAPI:

    # setup communication with bank server, but for dummy bank API, just sets up a single customer's info
    def __init__(self):
        self.account_values = {'1234567890':{'Savings Account':100,'Checking Account':200}}
        self.account_pins = {'1234567890':'1234'}

    # verify whether pin is correct for the associated card
    def check_pin(self, suspect_pin, suspect_card_info):
        if suspect_card_info in self.account_pins:
            if suspect_pin==self.account_pins[suspect_card_info]:
                return 1
            else:
                return 'Incorrect Pin'
        else:
            print(suspect_pin, suspect_card_info, self.account_pins)
            return 'No Account Associated With Card'

    # return account values
    def get_accounts(self, pin, card_info):
        check_result = self.check_pin(pin,card_info)
        if check_result==1:
            return self.account_values[card_info]
        else:
            return check_result

    # adjust the selected account by the directed amount
    def change_balance(self, change_amount, pin, card_info, account_name):
        check_result = self.check_pin(pin, card_info)
        if check_result==1:
            if account_name in self.account_values[card_info]:
                self.account_values[card_info][account_name] += change_amount
                return self.account_values[card_info][account_name]
            else:
                return 'Account Name Not Found'
        return check_result