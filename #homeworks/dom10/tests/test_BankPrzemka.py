from unittest import TestCase

from BankPrzemka import PromoSavingsAccount, BankSystem


class AccountTestCase(TestCase):
    def setUp(self):
        self.client_1 = BankAccount('Adam', 'Małysz', '111', 10000, 'PLN',1000)
        self.client_2 = BankAccount('Janusz', 'Wajs', '222', 50000, 'PLN',1000)
        self.Savings_client_1 = SavingsAccount('Jan', 'Oszczędny', '555', 10000, 'PLN',1000, 0.1)
        self.promo_Savings_client_1 = PromoSavingsAccount('Jan', 'Turbooszczędny', '666', 10000, 'PLN', 10000, 0.5, 500)

    def test_deposit_ok(self):
        balance_before = self.client_1.balance
        to_deposit = 100

        self.BankSystem.deposit('111', to_deposit)

        expected = balance_before + to_deposit
        self.assertEqual(expected, self.client_1.balance)

