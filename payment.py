from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def handle_payment(self, price: int):
        pass
