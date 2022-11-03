#! python3

### password_locker.py ###
### A simple and non-secure password manager ###

import sys
import pyperclip

passwords = {
    'e-mail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account)
