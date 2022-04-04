import pandas as pd
from typing import Dict, List, Any
import numpy as np
from math import radians, cos, sin, asin, sqrt, atan2
from geopy import distance


df = pd.read_csv('./eblocal_converts_test_v2.csv')

"""
Distance formula between two coordinates:
√[(long₂ - long₁)² + (lat₂ - lat₁)²]

Distance formula adjusted for curvature of the earth:
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c
where 	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
note that angles need to be in radians to pass to trig functions!
"""

#TEST
df = df[['dawa_id','name','municipality_name', 'longitude', 'latitude']]

test_data = [{'word': 'Viborg', 'entity_group': 'LOC', 'cluster_id' : 'A', 'lon_lat': (10,20)}, 
             {'word': 'Uldum', 'entity_group': 'ORG', 'cluster_id' : 'B', 'lon_lat':(10,30)},
             {'word': 'Solgårde', 'entity_group': 'LOC', 'cluster_id' : 'C', 'lon_lat':(10,40)}]

def compute_preds_distances(preds: List):
    
    df = pd.DataFrame(preds)
    # Make a distance matrix - 0 on the diagonal
    dist_matrix = pd.DataFrame(np.zeros(len(df) ** 2).reshape(len(df), len(df)), 
                               index = df.index, columns = df.word)
    def _get_distance(col):
        end = df.loc[col.name]['lon_lat']
        return df['lon_lat'].apply(distance.great_circle, args=(end,))

    dist_matrix = dist_matrix.apply(_get_distance, axis=1).T
    
    return dist_matrix

distance_matrix = compute_preds_distances(test_data)

# muni1 = 'Holbæk'
# muni2 = 'Høje-Taastrup'
# town1 = 'Vipperød'
# town2 = 'Taastrup'

# match_1 = df[df.municipality_name == muni1]
# match_2 = df[df.municipality_name == muni2]

# #sometimes the same place has two different coordinates.
# #Pick the first place in data.
# match_1 = match_1[match_1['name'] == town1]
# match_2 = match_2[match_2['name'] == town2]

# #Basic distance between two points in Euclidean plane.
# def calculate_simple_distance(match_1,match_2) -> float:
#     dist = np.sqrt((match_2['longitude'].item() - match_1['longitude'].item())**2 + (match_2['latitude'].item() - match_1['latitude'].item())**2)
#     return dist

# def haversine(lat1, lon1, lat2, lon2):
#     """
#     Calculate the great circle distance in kilometers between two points 
#     on the earth (specified in decimal degrees)
#     """
    
#     # convert decimal degrees to radians 
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

#     # haversine formula 
#     dlon = lon2 - lon1 
#     dlat = lat2 - lat1 
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a)) 
#     r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
#     return c * r

# #Adjusted for earth curvature in metres
# def calculate_complex_distance(match1, match2) -> float:
#     R = 6371e3 #convert to metres
#     o1 = match1['latitude'].item() * (np.pi/180) #φ, λ in radians
#     o2 = match2['latitude'].item() * (np.pi/180)
#     delta = (match2['longitude'].item() - match1['longitude'].item()) * (np.pi/180)
#     lambd = (match2['longitude'].item() - match1['longitude'].item()) * (np.pi/180)
#     a = (np.sin(delta/2)) * (np.sin(delta/2))+ \
#         (np.cos(o1)) * (np.cos(o2)) * \
#         (np.sin(lambd/2)) * (np.sin(lambd/2))
#     c = 2 * atan2(np.sqrt(a), np.sqrt(1-a))
#     distance = R * c
#     return distance    

# dist = calculate_complex_distance(match_1, match_2)

# if dist > 1:
#     print(f'The matches are too far away! {dist/1000} km, discarding prediction.')
# else:
#     print(f'Matches are within accepted range {dist/1000} km, processing prediciton')

# #Option 1
# lon1 = match_1['longitude'].astype(float).item()
# lat1 = match_1['latitude'].astype(float).item()
# lon2 = match_2['longitude'].astype(float).item()
# lat2 = match_2['latitude'].astype(float).item()

# print('numpy: ', haversine(lat1, lon1, lat2, lon2))

# #Option 2
# tuple1 = (match_1['longitude'].astype(float).item(), match_1['latitude'].astype(float).item())
# tuple2 = (match_2['longitude'].astype(float).item(), match_2['latitude'].astype(float).item())

# print('geopy: ',  distance.great_circle(tuple1,tuple2))

