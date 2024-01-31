class Ticket:
    """Stores ticket information"""
    def __init__(self,
                 origin,
                 destination,
                 travel_class,
                 journey_type,
                 valid_date,
                 price,
                 discount) -> None:
        self.origin = origin
        self.destination = destination
        self.travel_class = travel_class
        self.journey_type = journey_type
        self.valid_date = valid_date # tuple with two dates
        self.price = price
        self.discount = discount
