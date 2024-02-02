import pandas as pd
from tariefeenheden import Tariefeenheden
from ui_info import UIWay

class TicketPriceCalculator:

    @classmethod
    def _get_pricing_df(cls) -> pd.DataFrame:
        return pd.read_pickle("ticket_pricing.pkl")

    @staticmethod
    def get_price(ticket):
        tariefeenheden = Tariefeenheden.get_tariefeenheden(ticket.origin, ticket.destination)
        df = TicketPriceCalculator._get_pricing_df()

        price = df.loc[(df["TicketClass"] == ticket.travel_class) & (df["DiscountPercentage"] == ticket.discount)]
        price = price['Price'].values[0]
        price =  round(price * 0.02 * tariefeenheden, 2)

        if ticket.journey_type == UIWay.Return:
            price *= 2

        return price