import pandas as pd
from nbcc_loading.loading_data import Loading

class Wind(Loading):
    def __init__(self) -> None:
        Loading.__init__(self, loading_type="Wind")

    def __repr__(self) -> str:
        return f"Wind()"