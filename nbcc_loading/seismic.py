import pandas as pd
from nbcc_loading.loading_data import Loading

class Seismic(Loading):
    def __init__(self) -> None:
        Loading.__init__(self, loading_type="Seismic")

