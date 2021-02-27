from unittest import TestCase

from BankPrzemka import PromoSavingsAccount, BankSystem, SavingsAccount, BankAccount


class AccountTestCase(TestCase):
    def setUp(self):
        self.bank_system = BankSystem()
        self.client_1 = BankAccount('Adam', 'Małysz', '111', 10000, 'PLN', 1000)
        self.bank_system.add_account(self.client_1)
        self.client_2 = BankAccount('Janusz', 'Wajs', '222', 50000, 'PLN',1000)
        self.bank_system.add_account(self.client_2)
        self.savings_client_1 = SavingsAccount('Jan', 'Oszczędny', '555', 10000, 'PLN',1000, 0.1)
        self.bank_system.add_account(self.savings_client_1)
        self.promo_Savings_client_1 = PromoSavingsAccount('Jan', 'Turbooszczędny', '666', 10000, 'PLN', 10000, 0.5, 500)
        self.bank_system.add_account(self.promo_Savings_client_1)


    def test_deposit_ok(self):
        balance_before = self.client_1.balance
        id = self.client_1.id_no
        amount = 100

        self.bank_system.deposit(id, amount)

        expected = balance_before + amount
        self.assertEqual(expected, self.client_1.balance)

    def test_withdraw_ok(self):
        balance_before = self.client_2.balance
        id = self.client_2.id_no
        amount = 100

        self.bank_system.withdraw(id, amount)

        expected = balance_before - amount
        self.assertEqual(expected, self.client_2.balance)


    def test_transfer_ok(self):
        to_transfer = 500
        from_balance_before = self.client_1.balance
        to_balance_before = self.savings_client_1.balance
        id_from = self.client_1.id_no
        id_to = self.savings_client_1.id_no

        self.bank_system.transfer(id_from, id_to, to_transfer)

        expected_from_balance = from_balance_before - to_transfer
        self.assertEqual(self.client_1.balance, expected_from_balance)

        expected_to_balance = to_balance_before + to_transfer
        self.assertEqual(self.savings_client_1.balance, expected_to_balance)

    def test_withdraw_fail_not_enough_money(self):
        id = self.client_1.id_no
        amount = 50000

        self.bank_system.withdraw(id, amount)

        self.assertRaises('Za mało środków na koncie')
