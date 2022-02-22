from transformers import pipeline
import pandas as pd

from rapidfuzz.fuzz import partial_token_set_ratio
from fuzzup.fuzz import fuzz_it_up

TEXT = """
EU fremlægger som varslet nu en række muligheder for sanktioner mod Rusland.

Det fremgår af en udtalelse.

I 'pakken', som det kaldes i udtalelsen, er der specifikt fire forslag.

Sanktionerne skal ramme dem, der var involveret i den 'ulovlige' beslutning at anerkende udbryderregionerne.

Også banker, der finansierer det russiske militær og andre operationer i området skal rammes af EU's hammer.

Derudover foreslår EU at ramme Ruslands adgang til EU's kapital- og finansielle markeder for at begrænse finansieringen af 'eskalerende og aggressive tiltag'.

Til sidst vil EU også ramme handel i de to udbryderregioner til og fra EU.
"""

ner = pipeline(task='ner', 
                model='saattrupdan/nbailab-base-ner-scandi', 
                aggregation_strategy='first')
ner_output = ner(TEXT)

def tester(ner_output: list, to_dataframe: bool=False):
    ents = pd.DataFrame.from_records(ner_output)
    ents = ents.groupby("entity_group", dropna=False)
    out = {}
    for entity_type in ents.groups:
        group = ents.get_group(entity_type)
        clusters, _ = fuzz_it_up(group.word.tolist(), 
                                 scorer=partial_token_set_ratio, 
                                 to_dataframe=to_dataframe)
        out[entity_type] = clusters 
    #if to_dataframe:
    #    out = pd.concat(out, ignore_index=True)
    return out

t = tester(ner_output)
        
    
    
    




