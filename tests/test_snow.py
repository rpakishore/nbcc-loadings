from nbcc_loading.snow import Snow
import pytest
from typing import Generator, Any

@pytest.fixture(scope='module')
def snow_2020() -> Generator[Snow, Any, Any]:
    loads = Snow()
    loads(year=2020)
    yield loads
    del loads

@pytest.fixture(scope='module')
def snow_2015() -> Generator[Snow, Any, Any]:
    loads = Snow()
    loads(year=2015)
    yield loads
    del loads

def test_snow2020_values(snow_2020):
    loads: Snow = snow_2020
    df = loads.get()
    assert len(df) == 680
    provinces = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'NS', 'PE', 'NL', 'YT', 'NT', 'NU']
    num_cities= [108, 55, 31, 24, 230, 125, 18, 25, 4, 18, 9, 17, 16]
    
    assert list(df.loc[:, 'Province'].unique()) == provinces
    for idx, province in enumerate(provinces):
        assert len(df[df.loc[:, 'Province'] == province]) == num_cities[idx]
    
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['Ss'].iloc[0] == 1.7
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['Sr'].iloc[0] == 0.1

def test_Snow2020_by_gps(snow_2020):
    loads: Snow = snow_2020
    lat1 = 49.2508744
    long1 = -122.9032094
    snow_stations = loads.by_gps(latitude=lat1, longitude=long1, data_points=6)
    assert len(snow_stations) == 6

    assert snow_stations[0].location == 'Burnaby (Simon Fraser Univ.)'
    assert snow_stations[1].province == 'BC'
    assert snow_stations[2].latitude == 49.163
    assert snow_stations[3].longitude == -123.07
    assert snow_stations[4].Ss == 1.8
    assert snow_stations[4].Sr == 0.2

def test_Snow2020_by_location(snow_2020):
    loads: Snow = snow_2020
    snow_station = loads.by_location(city='Inukjuak')
    assert snow_station.Ss == 4.1
    assert snow_station.Sr == 0.2
    