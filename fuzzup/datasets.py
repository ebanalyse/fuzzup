import random

import pandas as pd
import numpy as np

from typing import List, Dict

def simulate_ner_data() -> List[Dict]:
    """Simulate NER data

    Returns:
        List[Dict]: Simulated NER data.
    """
    PERSONS = ['Donald Trump', 'Donald Trump', 'J. biden', 'joe biden', 'Biden', 'Bide', 'mark esper', 'Christopher c . miller', 'jim mattis', 'Nancy Pelosi', 'trumps', 'Trump', 'Donald', 'miller']
    # align format with output from Hugging Face `transformers` pipeline
    n = len(PERSONS)
    PERSONS_NER = pd.DataFrame(data = PERSONS, columns=['word'])
    PERSONS_NER["entity_group"] = "PER"
    PERSONS_NER["score"] = np.random.sample(n)
    PERSONS_NER["start"] = np.random.randint(100, size=n)
    PERSONS_NER["end"] = np.random.randint(100, size=n)
    placements = ["title", "lead", "body"]
    PERSONS_NER["placement"] = random.choices(placements, k=n)
    PERSONS_NER = PERSONS_NER.to_dict(orient="records")
    return PERSONS_NER