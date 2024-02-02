from datetime import datetime
from ticket_price_calculator import TicketPriceCalculator
from ui_info import UIWay

class Ticket:
    """Stores ticket information"""
    def __init__(self,
                 origin=None,
                 destination=None,
                 travel_class=None,
                 journey_type=None,
                 valid_date=None,
                 price=None,
                 discount=None,
                 use_different_date=False) -> None:
        self.origin = origin
        self.destination = destination
        self.travel_class = travel_class
        self.journey_type = journey_type
        self.valid_date = valid_date
        self.price = price
        self.discount = discount

        if origin is not None and destination is not None:
            self.price = TicketPriceCalculator.get_price(self)
        
        if self.journey_type == UIWay.Return or use_different_date is False:
            self.valid_date = datetime.today().strftime("%Y/%m/%d")
