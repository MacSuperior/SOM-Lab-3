from ticket import Ticket
from payment import Payment

class Sale:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def handle_payment(total_price, payment_method):
        p = Payment(total_price, payment_method)
        p.pay()
