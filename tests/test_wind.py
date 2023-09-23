from nbcc_loading.wind import Wind
import pytest
from typing import Generator, Any

@pytest.fixture(scope='module')
def wind_2020() -> Generator[Wind, Any, Any]:
    loads = Wind()
    loads(year=2020)
    yield loads
    del loads

def test_wind2020_values(wind_2020):
    loads: Wind = wind_2020
    df = loads.get()
    assert len(df) == 680
    provinces = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'NS', 'PE', 'NL', 'YT', 'NT', 'NU']
    num_cities= [108, 55, 31, 24, 230, 125, 18, 25, 4, 18, 9, 17, 16]
    
    assert list(df.loc[:, 'Province'].unique()) == provinces
    for idx, province in enumerate(provinces):
        assert len(df[df.loc[:, 'Province'] == province]) == num_cities[idx]
    
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['yr10'].iloc[0] == 0.29
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['yr50'].iloc[0] == 0.38

def test_Wind_by_gps(wind_2020):
    loads: Wind = wind_2020
    lat1 = 49.2508744
    long1 = -122.9032094
    wind_stations = loads.by_gps(latitude=lat1, longitude=long1, data_points=6)
    assert len(wind_stations) == 6

    assert wind_stations[0].location == 'Burnaby (Simon Fraser Univ.)'
    assert wind_stations[1].province == 'BC'
    assert wind_stations[2].latitude == 49.163
    assert wind_stations[3].longitude == -123.07
    assert wind_stations[4].yr10 == 0.35
    assert wind_stations[4].yr50 == 0.47
    
def test_Wind_by_location(wind_2020):
    loads: Wind = wind_2020
    wind_station = loads.by_location(city='Inukjuak')
    assert wind_station.yr10 == 0.37
    assert wind_station.yr50 == 0.48