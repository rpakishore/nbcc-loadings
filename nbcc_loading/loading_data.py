import pandas as pd
from pathlib import Path

SNOW_FILES = {
    2015: 'snow-2015.pickle'
}

WIND_FILES = {
    2015: 'wind-2015.pickle'
}

SEISMIC_FILES = {
}


def read_pickle(filepath: Path) -> pd.DataFrame:
    "returns the dataframe from specified filepath"
    return pd.read_pickle(filepath)

def read_pickle_from_data(filename: str) -> pd.DataFrame:
    "Returns the dataframe from specified file located in the data folder"
    filepath = Path(__file__).parent / "data" / filename
    return read_pickle(filepath)

class Loading:
    LOADING_FILES = {
        "Snow": SNOW_FILES,
        "Wind": WIND_FILES,
        "Seismic": SEISMIC_FILES
    }
    def __init__(self, loading_type: str) -> None:
        self.FILES = self.LOADING_FILES[loading_type]
        self.loading_type = loading_type

    def __str__(self) -> str:
        return f"{self.loading_type} loading class"

    def get(self, year: int) -> pd.DataFrame:
        "Returns the dataframe with snow load data for the year specified"
        if not year in self.FILES.keys():
            raise Exception(f"{year} data is not available. Acceptable options include: {[yr for yr in self.FILES.keys()]}")
        return read_pickle_from_data( filename=self.FILES.get(year) )
