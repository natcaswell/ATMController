from MenuState import MenuState

###################
# Main Program Loop: State machine using MenuState class as an object to track states and contain useful methods.
###################
menu = MenuState()

while 1:
    if menu.state=='Insert Card':
        menu.query_card()
    elif menu.state=='Enter Pin':
        menu.query_pin()
    elif menu.state=='Select Account':
        menu.query_account()
    elif menu.state == 'Select Account Action':
        menu.query_account_action()
    else:
        print('Invalid menu state: ', menu.state)
        menu.state = 'Insert Card'
