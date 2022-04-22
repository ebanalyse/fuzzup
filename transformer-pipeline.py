import logging

from ner.inference.predicter import NERPredicter
from rapidfuzz.fuzz import ratio, partial_token_set_ratio, token_set_ratio
import pandas as pd

from fuzzup.fuzz import fuzzy_cluster, compute_prominence, fuzzy_cluster_bygroup, compute_prominence_bygroup
from fuzzup.whitelists import (
    Cities, 
    Municipalities, 
    Neighborhoods,
    aggregate_to_cluster, 
    apply_whitelists, 
    format_output
)
from utils import get_news_data, clean_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# instantiate and load model
predicter = NERPredicter()
predicter.load_model('./Bizou/checkpoint-25000/')
c = Cities()
m = Municipalities()
n = Neighborhoods()
whitelists = [c,m,n]

# get article
article = get_news_data([9150838],
                        cols=["article_id", "title", "subtitle", "body_text"])
 
text = ",".join(article[["title", "subtitle", "body_text"]].values.tolist()[0])

text = clean_text(text)
preds = predicter.predict(text=text, sentence_based=True)

clusters = fuzzy_cluster_bygroup(preds, scorer=partial_token_set_ratio, cutoff=75)

clusters = compute_prominence_bygroup(clusters, weight_position=0.5)

matches = apply_whitelists(whitelists, clusters, scorer=ratio, score_cutoff=99, aggregate_cluster=True)
# to dataframe
l = []
for m in matches:
    l.append(pd.DataFrame.from_dict(matches.get(m)))
pd.concat(l, ignore_index=True)

format_output(matches, columns=["eblocal_code", "municipality_id"])
pd.DataFrame.from_dict(matches)




