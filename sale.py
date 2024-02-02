from ticket import Ticket
from payment import Payment

class Sale:
    def __init__(self, view) -> None:
        self.total_price = 0.0
        self.tickets = []
        self.view = view
    
    @staticmethod
    def handle_payment(total_price, payment_method):
        p = Payment(total_price, payment_method)
        p.pay()

    def add_ticket_to_total(self, ticket: Ticket):
        self.tickets.append(ticket)
        self.total_price += ticket.price
        self.total_price = round(self.total_price, 2)
    
    def delete_ticket_from_total(self, ticket: Ticket):
        self.tickets.remove(ticket)
        self.total_price -= ticket.price
        self.total_price = round(self.total_price, 2)
    
    def create_ticket(self):
        return Ticket(origin=self.view.from_station.get(),
                        destination=self.view.to_station.get(),
                        travel_class=self.view.travel_class.get(),
                        journey_type=self.view.way.get(),
                        valid_date=None,
                        price=None,
                        discount=self.view.discount.get(),
                        use_different_date=self.view.use_different_date.get())