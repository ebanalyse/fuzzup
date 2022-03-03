import requests
import pandas as pd
import re

# helper function
def clean_string(x):
    out = re.sub(r"\([^()]*\)", "", x)
    return out

def get_danish_politicians():
    """
    copy pasta from https://github.com/cfblaeb/politik
    """

    # ft.dk only allows 100 rows per call
    table='Aktør'
    url = f'http://oda.ft.dk/api/{table}'
    totalcount = int(requests.get(url, params={"$inlinecount": "allpages"}).json()['odata.count'])
    ccount = 0
    print(f"# records: {totalcount}")
    
    results = []
    while ccount < totalcount:
        r = requests.get(url, params={"$skip": ccount})
        for row in r.json()['value']:
            if all([row.get('slutdato') is None,
                    row.get('startdato') is not None,
                    row.get('fornavn') is not None,
                    row.get('efternavn') is not None]):
                results.append(row)

        ccount += 100
        if ccount % 1000 == 0:
            print(f"# records processed: {ccount}/{totalcount}")

    print(f"Number of politicians identified: {len(results)}")

    # extract names    
    names = [x.get('fornavn') + " " + x.get('efternavn') for x in results]
    names = [clean_string(x).strip() for x in names]
    names.sort()
    
    # convert to fuzzup dict format
    names = {x: {} for x in names}
    
    return names