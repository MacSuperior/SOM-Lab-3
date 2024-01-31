from typing import List
import pandas as pd

class Tariefeenheden:

    @staticmethod
    def _get_tariefeenheden_df() -> None:
        return pd.read_pickle("tariefeenheden.pkl")


    @staticmethod
    def get_stations() -> List[str]:
        return ["Utrecht Centraal",
                "Gouda",
                "Geldermalsen",
                "Hilversum",
                "Duivendrecht",
                "Weesp"]


    @staticmethod
    def get_tariefeenheden(origin, destination):
        df = Tariefeenheden._get_tariefeenheden_df()
        tariefeenheden = df.loc[(df["From"] == origin) & (df["To"] == destination)]
        tariefeenheden = tariefeenheden["Tariefeenheden"].values[0]
        return tariefeenheden
