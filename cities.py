import requests
import pandas as pd
 
def get_byer():
    """Get all byer in DK"""
    url = 'https://api.dataforsyningen.dk/steder?hovedtype=Bebyggelse&undertype=by'
    byer = requests.get(url).json()
    records = []
    for by in byer:
        kommuner = [kommune['navn'] for kommune in by['kommuner']]
        if len(kommuner) == 1:
            kommuner = kommuner[0]
        records.append(
            {
                'navn': by['primærtnavn'],
                'indbyggerantal': by['egenskaber']['indbyggerantal'],
                'kommune': kommuner
            }
        )
    df = pd.DataFrame(records)
    return df
​
byer = get_byer()
kommuner = byer.kommune.tolist()
kommuner = [[x] if isinstance(x, str) else x for x in byer]
kommuner = [item for sublist in byer for item in sublist]
kommuner = 