from datetime import datetime as dt

class Ticket():
    def __init__(ticket_type: str, journey_type: str, ticket_amount: int, dep_station: str, dest_station: str, price: float, date: dt, self):
        self.ticket_type = ticket_type
        self.journey_type = journey_type
        self.ticket_amount = ticket_amount
        self.dep_station = dep_station
        self.dest_station = dest_station
        self.price = price
        self.date = date

