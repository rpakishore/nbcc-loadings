from nbcc_loading.loading_data import Loading
from nbcc_loading.loading_data import _distance_bet_coords
from dataclasses import dataclass

@dataclass
class SnowStation:
    location: str
    province: str
    latitude: float
    longitude: float
    Ss: float
    Sr: float
    
    def distance(self, latitude: float, longitude: float) -> float:
        "Returns distance in KM to the specified coordinates from the station"
        return _distance_bet_coords(lat1=self.latitude, long1=self.longitude, 
                                    lat2=latitude, long2=longitude)

class Snow(Loading):
    def __init__(self) -> None:
        Loading.__init__(self, loading_type="Snow")
    
    def by_location(self, city: str, province: str|None = None, 
                    year: int|None = None) -> SnowStation:
        df = self.get(year=year)
        if province:
            df = df[df.Province == province.strip().upper()]
            assert len(df)>=1, f'{province} is not a valid Province'
        df = df[df.Location == city]
        assert len(df)>=1, f'{city} is not a valid city'

        return SnowStation(location=df.iloc[0,:]['Location'], 
                            province=df.iloc[0,:]['Province'],
                            latitude=df.iloc[0,:]['Latitude'],
                            longitude=df.iloc[0,:]['Longitude'],
                            Ss=df.iloc[0,:]['Ss'],
                            Sr=df.iloc[0,:]['Sr'])
        
    def by_gps(self, latitude: float, longitude: float, year: int|None = None, 
                data_points: int = 5) -> list[SnowStation]:
        df = self.get(year=year)
        df = df.copy()
        df['Distance'] = df.apply(lambda row: _distance_bet_coords(
                                        lat1=latitude, long1=longitude,
                                        lat2= row['Latitude'], long2=row['Longitude']), 
                                    axis=1)
        df = df.sort_values(by='Distance', ascending=True)
        
        snow_stations: list[SnowStation] = []
        for _, row in df.iloc[:data_points,:].iterrows():
            snow_stations.append(
                SnowStation(
                    location=row['Location'],
                    province=row['Province'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    Ss=row['Ss'],
                    Sr=row['Sr']
                    )
            )
        return snow_stations