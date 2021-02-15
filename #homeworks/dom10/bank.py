# Wykorzystując paradygmant programowania obiektowego zamodeluj klasę(y) potrzebne do operacji bankowych:
# Możliwość utworzenia nowego konta, które przechowuje informacje dotyczące klienta, stanu konta, oraz waluty w jakiej przechowywane są środki.
# Wpłaty środków.
# Wypłaty środków.
# Ustalanie limitów wypłat. ?Nie wiem od czego zacząć?
# Przelew z konta A na konto B.
# Dodatkowo dla chętnych: historia tranzakcji tj. wpłaty, wypłaty, przelewy przychodzące i wychodzące w formie raportu do pliku lub podsumowania na ekranie

class Bank_account:
    def __init__(self, client_firstname, client_lastname, account_id_no, account_balance, account_currency):
        self.firstname = client_firstname
        self.lastname = client_lastname
        self.id_no = account_id_no
        self.balance = account_balance
        self.currency = account_currency

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.id_no} {self.balance} {self.currency}'


class Bank_system:
    def __init__(self):
        self.account_list = []

    def add_account(self, Bank_account):
        self.account_list.append(Bank_account)

    def display_all(self):
        for Bank_account in self.account_list:
            print(Bank_account)

    def deposit (self, id_no, amount):
        for Bank_account in self.account_list:
            if id_no == Bank_account.id_no:
                Bank_account.balance = Bank_account.balance + amount

    def withdraw(self, id_no, amount):
        for Bank_account in self.account_list:
            if id_no == Bank_account.id_no:
                if Bank_account.balance >= amount:
                    Bank_account.balance = Bank_account.balance - amount
                else:
                    print('Za mało środków na koncie')

    def transfer(self, id_no_from, id_no_to, amount): # Czy mozna
        for Bank_account in self.account_list:
            if id_no_from == Bank_account.id_no and Bank_account.balance >= amount:
               # print('ok')  # dodane roboczo
                # Bank_account.balance = Bank_account.balance - amount
                # if id_no_to == Bank_account.id_no:
                #     Bank_account.balance = Bank_account.balance + amount
            else:
                print('Konto z jakiego chcesz przelać środki nie istnieje lub ma za mało środków')

if __name__ == '__main__':
    client_1 = Bank_account('Adam', 'Małysz', '111', 10000, 'PLN')
    client_2 = Bank_account('Janusz', 'Wajs', '222', 50000, 'PLN')
    client_3 = Bank_account('Robert', 'Kubica', '333', 5000, 'PLN')
    client_4 = Bank_account('Michał', 'Bajor', '444', 1000000, 'PLN')

    bank_system_of_mybank = Bank_system()
    bank_system_of_mybank.add_account(client_1)
    bank_system_of_mybank.add_account(client_2)
    bank_system_of_mybank.add_account(client_3)
    bank_system_of_mybank.add_account(client_4)
    bank_system_of_mybank.display_all()
# Wpłaty środków.
    bank_system_of_mybank.deposit ('111', 100)
    bank_system_of_mybank.display_all()
# Wypłaty środków.
    bank_system_of_mybank.withdraw('333', 5001)
    bank_system_of_mybank.withdraw('333', 4999)
    bank_system_of_mybank.display_all()
# # Ustalanie limitów wypłat. ????
# ?????
# Przelew z konta A na konto B.
    bank_system_of_mybank.transfer('222', '444', 10)
    bank_system_of_mybank.display_all()


