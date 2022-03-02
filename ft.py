import requests
import pandas as pd

def scrape_politicians():
    """
    copy pasta from 
    """

    # ft.dk tillader kun at du henter 100 rækker per kald
    # derfor så starte vi med at spørge om hvor mange rækker der er i alt
    table='Aktør'
    url = f'http://oda.ft.dk/api/{table}'
    totalcount = int(requests.get(url, params={"$inlinecount": "allpages"}).json()['odata.count'])
    ccount = 0
    print(f"# records: {totalcount}")
    # herefter henter vi indtil vi har hentet alt
    
    results = []
    while ccount < totalcount:
        r = requests.get(url, params={"$skip": ccount})
        for row in r.json()['value']:
            if row.get('slutdato') is None and row.get('startdato') is not None:
                results.append(row)

        ccount += 100
        if ccount % 1000 == 0:
            print(f"# records processed: {ccount}/{totalcount}")

    print(f"Number of politicians identified: {len(results)}")
    return results

pols = scrape_politicians()

            

            
