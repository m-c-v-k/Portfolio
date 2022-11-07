#! Python3

# Project 11 - Make your own Bank!
# Creating a bank.

class Account:
    """ Account parent class.
    """

    def __init__(self, name, balance, min_balance):
        """ Constructor function.

        Args:
            name (string): A string containing a name.
            balance (int): An int containing current account balance.
            min_balance (int): An int containing minimum account balance.
        """

        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        """ Handles depositions into account.

        Args:
            amount (int): Adds amount to account balance.
        """

        self.balance += amount

    def withdraw(self, amount):
        """ Handles withdraws from the account.

        Args:
            amount (int): Amount to be deducted from the account.
        """

        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        """ Handles account statements.
        """
        print(f"Account Balance: £{self.balance}")


class Current(Account):
    """ Current account class.

    Args:
        Account (class): Parent class for accounts.
    """

    def __init__(self, name, balance):
        """ Constructor function for current account.

        Args:
            name (string): Name of the account holder.
            balance (int): An integer with the current account balance.
        """

        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        """ Handles printing

        Returns:
            string: States account holder as well as balance.
        """

        return f"{self.name} current account: Balance £{self.balance}"


class Savings(Account):
    """ Savings account class.

    Args:
        Account (class): Parent class for accounts.
    """

    def __init__(self, name, balance):
        """ Constructor function for savings account.

        Args:
            name (string): Name of the account holder.
            balance (int): An integer with the current account balance.
        """

        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        """ Handles printing

        Returns:
            string: States account holder as well as balance.
        """

        return f"{self.name} savings account: Balance £{self.balance}"


# Simple functionality tests
x = Current("Marcus", 500)
print(x.name)
x.deposit(300)
print(x.balance)
x.statement()
x.withdraw(200)
x.statement()
print(x)

z = Savings("Tom", 300)
print(z)
z.withdraw(300)
z.statement()
z.withdraw(1)
