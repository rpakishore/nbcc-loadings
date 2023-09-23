import pandas as pd
from pathlib import Path
from typing import Literal
import geopy.distance

SNOW_FILES = {
    2020: 'snow-2020.pkl',
    2015: 'snow-2015.pkl'
}

WIND_FILES = {
    2020: 'wind-2020.pkl',
    2015: 'wind-2015.pkl'
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
    LOADING_FILES: dict[str,dict[int, str]] = {
        "Snow": SNOW_FILES,
        "Wind": WIND_FILES,
        "Seismic": SEISMIC_FILES
    }
    def __init__(self, loading_type: Literal['Snow', 'Wind', 'Seismic']) -> None:
        self.FILES = self.LOADING_FILES[loading_type]
        self.loading_type = loading_type
        self.YEAR: int = 2015

    def __str__(self) -> str:
        return f"{self.loading_type} loading class"
    
    def __repr__(self) -> str:
        return f"{self.loading_type}() Class Instance"

    def get(self, year: int|None = None) -> pd.DataFrame:
        "Returns the dataframe with snow load data for the year specified"
        if year is None:
            year = self.YEAR
        year = int(year)
        if year not in self.FILES.keys():
            raise Exception(f"{year} data is not available. Acceptable options include: {[yr for yr in self.FILES.keys()]}")
        return read_pickle_from_data( filename=self.FILES.get(year)) # type: ignore
    
    def set_year(self, year: int) -> pd.DataFrame:
        if year not in self.FILES.keys():
            raise Exception(f"{year} data is not available. Acceptable options include: {[yr for yr in self.FILES.keys()]}")
        self.YEAR = year
        return self.get(year = self.YEAR)
    
    def __call__(self, year: int) -> pd.DataFrame:
        return self.set_year(year=year)
    

def _distance_bet_coords(lat1: float, long1: float, lat2: float, long2:float) -> float:
    coord1 = (lat1, long1)
    coord2 = (lat2, long2)
    return geopy.distance.distance(coord1, coord2).km