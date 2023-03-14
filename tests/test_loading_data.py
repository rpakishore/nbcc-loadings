from nbcc_loading.loading_data import *

def test_snow2020():
    loads = Loading('Snow')
    df = loads.get('2020')
    assert len(df) == 680
    provinces = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'NS', 'PE', 'NL', 'YT', 'NT', 'NU']
    num_cities= [108, 55, 31, 24, 230, 125, 18, 25, 4, 18, 9, 17, 16]
    
    assert list(df.loc[:, 'Province'].unique()) == provinces
    for idx, province in enumerate(provinces):
        assert len(df[df.loc[:, 'Province'] == province]) == num_cities[idx]
    
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['Ss'].iloc[0] == 1.7
    assert df[df.loc[:, 'Location'] == 'Ashcroft']['Sr'].iloc[0] == 0.1