from payment import Payment, abstractmethod

class Card(Payment):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def begin_transaction(self, amount: float) -> int:
        pass

    @abstractmethod
    def end_transaction(self, id: int) -> bool:
        pass

    @abstractmethod
    def cancel_transaction(self, id: int):
        pass

    def handle_payment(self, price: int):
        self.connect()
        id: int = self.begin_transaction(round(price, 2))
        self.end_transaction(id)
        self.disconnect()
