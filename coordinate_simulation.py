import pandas as pd
from typing import Dict, List, Any
import numpy as np
from math import radians, cos, sin, asin, sqrt, atan2
from geopy import distance


df = pd.read_csv("./eblocal_converts_test_v2.csv")

"""
Distance formula between two coordinates:
√[(long₂ - long₁)² + (lat₂ - lat₁)²]

Distance formula adjusted for curvature of the earth:
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c
where 	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
note that angles need to be in radians to pass to trig functions!
"""

whitelist_data = {
    "city": [
        {
            "word": "Viborg",
            "entity_group": "LOC",
            "cluster_id": "A",
            "matches": ["Visborg", "Viborg"],
            "mappings": [
                {
                    "municipality": ["Mariagerfjord"],
                    "eblocal_code": "12337669-ca46-6b98-e053-d480220a5a3f",
                    "lon_lat": (20, 11),
                },
                {
                    "municipality": ["Viborg"],
                    "eblocal_code": "12337669-ba55-6b98-e053-d480220a5a3f",
                    'lon_lat':(10,33)
                },
            ],
        }
    ],
    "municipality": [],
    "neighborhood": [
        {
            "word": "Solgårde",
            "entity_group": "LOC",
            "cluster_id": "C",
            "matches": ["Solgårde"],
            "mappings": [
                {
                    "eblocal_code": "12337669-ba5f-6b98-e053-d480220a5a3f",
                    "lon_lat": (20, 12),
                }
            ],
        }
    ],
}

def compute_preds_distances2(preds:Dict):
    
    coord_data = []
    
    for whitelist in preds:
        for matches in preds[whitelist]:
            #unpack values in list of dictionaries
            for mapping in matches['mappings']:
                eblocal_code = mapping['eblocal_code']
                lon_lat = mapping['lon_lat']
                data = {"eblocal_code":eblocal_code, "lon_lat":lon_lat}            
                coord_data.append(data)
    df = pd.DataFrame(coord_data)

    dist_matrix = pd.DataFrame(
    np.zeros(len(df) ** 2).reshape(len(df), len(df)),
    index=df.index,
    columns=df.eblocal_code,
    )

    def _get_distance(col):
        
        end = df.loc[col.name]["lon_lat"]
        return df["lon_lat"].apply(distance.great_circle, args=(end,))

    dist_matrix = dist_matrix.apply(_get_distance, axis=1).T
    
    return dist_matrix

print(compute_preds_distances2(whitelist_data))