from creditcard import CreditCard
from debitcard import DebitCard
from coin_machine import IKEAMyntAtare2000
from ui_info import UIPayment

class Payment:
    def __init__(self, total_price, payment_method) -> None:
        self.total_price = total_price
        self.payment_method = payment_method


    def pay(self):
        if self.total_price == 0.0:
            return
        if self.payment_method == UIPayment.credit_card:
            self.total_price += CreditCard.fee
            self._pay_by_creditcard()
        
        elif self.payment_method == UIPayment.debit_card:
            self._pay_by_debitcard()

        elif self.payment_method == UIPayment.cash:
            self._pay_by_cash()
    

    def _pay_by_cash(self):
        coin_machine = IKEAMyntAtare2000()
        coin_machine.starta()
        coin_machine.betala(int(round(self.total_price * 100)))
        coin_machine.stoppa()


    def _pay_by_creditcard(self):
        card = CreditCard()
        card.connect()
        card_id: int = card.begin_transaction(round(self.total_price, 2))
        card.end_transaction(card_id)
        card.disconnect()
    

    def _pay_by_debitcard(self):
        card = DebitCard()
        card.connect()
        card_id: int = card.begin_transaction(round(self.total_price, 2))
        card.end_transaction(card_id)
        card.disconnect()
