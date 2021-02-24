from unittest import TestCase

from BankPrzemka import PromoSavingsAccount, BankSystem, SavingsAccount, BankAccount


class AccountTestCase(TestCase):
    def setUp(self):
        self.bank_system = BankSystem()
        self.client_1 = BankSystem.add_account('Adam', 'Małysz', '111', 10000, 'PLN',1000)
        # self.client_2 = BankAccount('Janusz', 'Wajs', '222', 50000, 'PLN',1000)
        # self.Savings_client_1 = SavingsAccount('Jan', 'Oszczędny', '555', 10000, 'PLN',1000, 0.1)
        # self.promo_Savings_client_1 = PromoSavingsAccount('Jan', 'Turbooszczędny', '666', 10000, 'PLN', 10000, 0.5, 500)
        # self.bank_system = BankSystem()

    def test_deposit_ok(self):
        balance_before = self.client_1.balance
        amount = 100

        self.bank_system.depositclient_1z(client_1, amount)

        expected = balance_before + amount
        self.assertEqual(expected, self.client_1.balance)

