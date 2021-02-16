
# Wykorzystując paradygmant programowania obiektowego zamodeluj klasę(y) potrzebne do operacji bankowych:
# Możliwość utworzenia nowego konta, które przechowuje informacje dotyczące klienta, stanu konta, oraz waluty w jakiej przechowywane są środki.
# Wpłaty środków.
# Wypłaty środków.
# Ustalanie limitów wypłat. ?Nie wiem od czego zacząć?
# Przelew z konta A na konto B.
# Dodatkowo dla chętnych: historia tranzakcji tj. wpłaty, wypłaty, przelewy przychodzące i wychodzące w formie raportu do pliku lub podsumowania na ekranie

class BankAccount:
    def __init__(self, client_firstname, client_lastname, account_id_no, account_balance, account_currency, account_withdraw_limit):
        self.firstname = client_firstname
        self.lastname = client_lastname
        self.id_no = account_id_no
        self.balance = account_balance
        self.currency = account_currency
        self.withdraw_limit = account_withdraw_limit

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.id_no} {self.balance} {self.currency}'


class BankSystem:
    def __init__(self):
        self.accounts = dict()

    def add_account(self, bank_account):
        self.accounts[bank_account.id_no] = bank_account

    def display_all(self):
        for bank_account_id, bank_account in self.accounts.items():
            print(bank_account)

    def deposit(self, id_no, amount):
        bank_account = self.accounts[id_no]
        bank_account.balance = bank_account.balance + amount

    def withdraw(self, id_no, amount,):
        bank_account = self.accounts[id_no]
        if bank_account.balance>= amount:
            if amount < bank_account.withdraw_limit:
                bank_account.balance = bank_account.balance - amount
            else:
                print('Wypłata powyżej limitu')
        else:
            print('Za mało środków na koncie')

    def transfer(self, id_no_from, id_no_to, amount):
        from_account = self.accounts[id_no_from]
        to_account = self.accounts[id_no_to]
        if from_account.balance >= amount:
            from_account.balance = from_account.balance - amount
            to_account.balance = to_account.balance + amount
        else:
            print('Za mało środków na koncie')


if __name__ == '__main__':
    client_1 = BankAccount('Adam', 'Małysz', '111', 10000, 'PLN',1000)
    client_2 = BankAccount('Janusz', 'Wajs', '222', 50000, 'PLN',1000)
    client_3 = BankAccount('Robert', 'Kubica', '333', 5000, 'PLN',1000)
    client_4 = BankAccount('Michał', 'Bajor', '444', 1000000, 'PLN',1000)
    print('Dodanie kont')
    bank_system_of_mybank = BankSystem()
    bank_system_of_mybank.add_account(client_1)
    bank_system_of_mybank.add_account(client_2)
    bank_system_of_mybank.add_account(client_3)
    bank_system_of_mybank.add_account(client_4)
    bank_system_of_mybank.display_all()
    print('Wpłaty środków')
    bank_system_of_mybank.deposit('111', 100)
    bank_system_of_mybank.display_all()
    print('Wypłaty środków')
    bank_system_of_mybank.withdraw('333', 5001)
    bank_system_of_mybank.withdraw('333', 4999)
    bank_system_of_mybank.withdraw('333', 999)
    bank_system_of_mybank.display_all()
    # # Ustalanie limitów wypłat. ????
    # ?????
    # Przelew z konta A na konto B.
    print('Przelew środków')
    bank_system_of_mybank.transfer('222', '444', 50000)
    bank_system_of_mybank.display_all()
