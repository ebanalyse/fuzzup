import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict, Callable
import numpy as np
from fuzzup.fuzz import fuzzy_cluster_bygroup, fuzzy_cluster, compute_prominence_bygroup, compute_prominence_placement
from rapidfuzz.fuzz import (
    ratio,
    partial_ratio,
    partial_ratio_alignment,
    token_sort_ratio,
    partial_token_sort_ratio,
    token_set_ratio,
    partial_token_set_ratio,
    token_ratio,
    partial_token_ratio,
    WRatio,
    QRatio,
)
import re
import html
import matplotlib.pyplot as plt
from ner.inference import NERPredicter
from fuzzup.whitelists import EBLocalNames, Municipalities, apply_whitelists
from bayes_opt import BayesianOptimization, UtilityFunction

class FuzzEvaluater():
    
    def __init__(self,train_df:pd.DataFrame, mode:str, model_path:str):
        self.FUZZUP_SCORERS = {
            0: ratio,
            1: partial_ratio,
            2: partial_token_set_ratio,
        }
        
        self.mode = mode
        self.train_df = train_df
        self.preds_dict = None
        self.model_path = model_path
        self.model = NERPredicter()
        self.whitelists = [EBLocalNames(), Municipalities()]
        
    def preproces_dataset(self,
                          train: pd.DataFrame, 
                          cutoff: int, 
                          scorer: object, 
                          weight_pos: int = 1, 
                          eval:str = 'whitelist',
                          **kwargs) -> List[Dict]:
        """_summary_

        Args:
            train (pd.DataFrame): pandas dataframe
            cutoff (int): _description_
            scorer (object): _description_
            weight_pos (int, optional): _description_. Defaults to 1.
            eval (str, optional): _description_. Defaults to 'whitelist'.


        Returns:
            List[Dict]: A list of predictions for a set of articles in a pandas dataframe
        """        
        self.preds_dict = defaultdict(lambda: {})
        processed_df = pd.DataFrame()
        
        with tqdm(total=train["article_id"].nunique()) as pbar:
            for article in np.unique(train["article_id"]):
                pbar.update(1)
                for index, row in train[train["article_id"] == article].iterrows():
                    data = dict(row)
                    # Append predictions within an article (List of dictionaries / predictions for each article)
                    row['preds'] = self._ner_predict(data)

                    processed_df = processed_df.append(row)
                    #self.preds_dict[article].update(self._ner_predict(data))
        final_df = pd.concat([processed_df,processed_df['preds'].explode().apply(pd.Series)], axis=1)
        final_df = final_df.drop(columns=['preds'])
        return final_df
    
    def _ner_predict(self, data: Dict) -> List[Dict]:
        if 'subtitle' not in data:
            data['subtitle'] = ''
        
        try:
            #Concat the strings that the model have to predict on. 
            text = self.clean_text(data['title'] + '. ' + data['subtitle'] + '. ' + data['body_text'])
        except:
            data['subtitle'] = ''
            text = self.clean_text(data['title'] + '. ' + data['subtitle'] + '. ' + data['body_text'])
            pass
        
        self.model.load_model(self.model_path)
        
        #Curate predictions from NER and Fuzzup    
        ner_predictions = self.model.predict(text, sentence_based=True)
        self._text_segment_adder(data, ner_predictions)
        # fuzzy_prediction = fuzzy_cluster_bygroup(ner_prediction, **kwargs)
        # prominence_prediction = compute_prominence_bygroup(fuzzy_prediction,  **kwargs)
        # whitelist_clusters = apply_whitelists(whitelists=self.whitelists, clusters=prominence_prediction, aggregate_cluster=True, **kwargs)
        # self.preds_dict[data['article_id']]['true_value_city'] = data['NER-matches_city']
        # self.preds_dict[data['article_id']]['true_value_municipality'] = data['NER-matches_municipality']
        
        return ner_predictions
    
    def _text_segment_adder(self, json_data: Dict, preds_out: List[Dict]):
        # This will probably require that each piece of text is seperated by a \n
        for pred in preds_out:
            lens = [
                len(json_data["title"]),
                len(json_data["subtitle"]),
                len(json_data["body_text"]),
            ]
            if pred["start"] <= lens[0]:
                pred["text_segment"] = "title"
            elif pred["start"] <= lens[0] + lens[1]:
                pred["text_segment"] = "subtitle"
            elif pred["start"] <= lens[0] + lens[1] + lens[2]:
                pred["text_segment"] = "body_text"
        return preds_out
    
    def clean_text(self, text: str) -> str:
        text = html.unescape(text) # Unescape HTML tags, e.g. &quot; -> ' 
        text = re.sub(r'[«»„"‟"❝❞〝〞〟＂‹›❮❯‚"‛❛❜´`"\'"]', '"', text) # Remove quotation marks
        text = re.sub(r'[‐‑‒–—―〜〰﹘﹣－]', '-', text) # Remove unusual dashes
        text = text.replace('\u200b', ' ').strip() # Remove zero width space
        text = text.replace('\xa0', ' ').strip() # Remove non-breaking space
        text = text.replace('--------- SPLIT ELEMENT ---------', ' ').strip() # Remove horizontal separators
        text = re.sub(r'\s-\s', ' ', text) # Remove seperating dashes
        text = re.sub(r'<.+?>', ' ', text) # Remove HTML tags
        text = re.sub(r'\\n', ' ', text) # Remove visible newlines
        text = re.sub(r'\n', ' ', text) # Remove invisible newlines
        text = re.sub(r'\s{2,}', ' ', text) # Remove excessive spacing

        return text
        
            
def load_dataframe() -> pd.DataFrame:
    train = pd.read_excel("./annotated_dump.xlsx")
    #Only need the ones with comment
    train = train[~train.Kommentar.isna()]
    
    return train

train_df = load_dataframe()
fuzz_eval = FuzzEvaluater(train_df, 'jaccard', 'Bizou/checkpoint-25000')

final_df = fuzz_eval.preproces_dataset(train_df, cutoff = 98, scorer=WRatio, weight_pos = 1, eval='whitelist')

final_df.to_excel('./processed_annotated_dump.xlsx')
__import__('pdb').set_trace()

# def _assert_fuzz_json(json_data):
#     if not all (key in json_data for key in ("title","body")):
#         raise ValueError('One of title or body not found in request')
        
#     if 'lead' not in json_data or type(json_data['lead']) is not str:
#         json_data['lead'] = '' #Can be empty since not all articles have one
               
#     if 'sentence_based' not in json_data:
#         json_data['sentence_based'] = True
        
#     return json_data

# def _text_segment_adder(json_data, preds_out):
#     #This will probably require that each piece of text is seperated by a \n
#     for pred in preds_out:
#         lens = [len(json_data['title']), len(json_data['lead']), len(json_data['body'])]
#         if pred['start'] <= lens[0]:
#             pred['text_segment'] = 'title'
#         elif pred['start'] <= lens[0] + lens[1]:
#             pred['text_segment'] = 'lead'
#         elif pred['start'] <= lens[0] + lens[1] + lens[2]:
#             pred['text_segment'] = 'body'
#         else:
#             pred['text_segment'] = 'body'
#     return preds_out


# def _predict(preds: List[Dict], cutoff, scorer, weight_pos, json_data, **kwargs) -> Dict:
#     res = defaultdict(lambda: {})
    
#     json_data = _assert_fuzz_json(json_data)
    
#     fuzzy_preds = fuzzy_cluster_bygroup(
#         preds, cutoff=cutoff, scorer=FUZZUP_SCORERS[scorer]
#     )
    
#     fuzzy_preds = _text_segment_adder(json_data, fuzzy_preds)

#     try:
#         fuzzy_preds = compute_prominence_placement(fuzzy_preds, weight_position=weight_pos, **kwargs)
#     except:
#         __import__('pdb').set_trace()
    
#     for i, fuzzy_pred in enumerate(fuzzy_preds):
#         res[i].update(
#             {
#                 "word": fuzzy_pred["word"],
#                 "pred": fuzzy_pred["cluster_id"],
#                 "true_value": fuzzy_pred["true_value"],
#                 "prominence_rank": fuzzy_pred["prominence_rank"],
#                 "prominence_score": fuzzy_pred["prominence_score"],
#                 "prominent": fuzzy_pred["prominent"],
#             }
#         )
#     return res


# def process_dataset(train: pd.DataFrame, cutoff, scorer, weight_pos=1, eval = 'whitelist',**kwargs) -> List[Dict]:
#     preds_dict = defaultdict(lambda: {})
#     with tqdm(total=train["article_id"].nunique()) as pbar:
#         for article in np.unique(train["article_id"]):
#             pbar.update(1)
#             preds_list = []
#             json_data = {}
#             for index, row in train[train["article_id"] == article].iterrows():
#                 row["true_value"] = row["NER-matches_city"]
#                 preds_list.append(dict(row))
#             json_data['title'] = row['title']
#             json_data['body'] = row['body_text']
#             if 'lead' in row is not None:
#                 json_data['lead'] = row['subtitle']
#             preds_dict[article].update(_predict(preds_list, cutoff, scorer, weight_pos, json_data, **kwargs))
#     return preds_dict

# def evaluate_fuzzy_matching(preds_dict: Dict, mode: str = "jaccard") -> float:
#     """Just loops through the preds dict and aggregates their evaluations"""

#     if mode == "jaccard":
#         accuracies = {}
#         diagnosis_dict = {}
#         for article in preds_dict.keys():
#             preds_set = set()
#             true_set = set()
#             for preds in preds_dict[article].values():
#                 preds_set.add(preds["pred"].lower())
#                 true_set.add(preds["true_value"].lower())
#             if len(preds_set) != 0 and len(true_set) != 0:
#                 accuracy = round(
#                     len(preds_set.intersection(true_set))
#                     / len(preds_set.union(true_set)),
#                     2,
#                 )
#                 if len(preds_set - true_set) != 0:
#                     diagnosis_dict[article] = {
#                         "preds_set": preds_set,
#                         "true_set": true_set,
#                         "misses": preds_set - true_set,
#                     }
#             else:
#                 pass
#             accuracies[article] = accuracy
#         return (
#             sum(accuracies.values()) / len(accuracies),
#             diagnosis_dict,
#         )  # Return the mean accuracy of all jaccard indices

#     elif mode == "dice":
#         res = {}

#         for article in preds_dict.values():
#             pred_set = set()
#             true_set = set()
#             for preds in article.values():
#                 if preds["pred"] not in pred_set:
#                     pred_set.add(preds["pred"])
#                 if preds["true_value"] not in true_set:
#                     true_set.add(preds["true_value"])
#             dice_similarity = (2 * len(np.intersect1d(pred_set, true_set))) / (
#                 len(pred_set) ** 2 + len(true_set) ** 2
#             )

#     else:
#         raise ValueError('Please set mode arg to either "jaccard" or "dice"')
    

# def calculate_f1(TN:float, TP:float, FN:float, FP:float) -> float:
#     precision = TP/(TP+FP)
#     recall = TP/(TP+FN)
#     f1 = 2 * (precision * recall) / (precision + recall)    
#     return f1

# def evaluate_prominence2(preds_dict: Dict, mode: str = "jaccard") -> float:
#     TN = 0
#     TP = 0
#     FN = 0
#     FP = 0
#     # 2 * (Precision * Recall) / (Precision + Recall)
#     for article in preds_dict.values():
#         for preds in article.values():
#             if preds['prominence_score'] >= 10:
#                 if preds['prominent'] == 1:
#                     TP += 1
#                 else:
#                     FP += 1
#             if preds['prominence_score'] < 10:
#                 if preds['prominent'] == 0:
#                     TN += 1
#                 else:
#                     FN += 1
    
#     print('CONFUSION MATRIX: \n')
#     print(np.array(([TP, FP],[FN, TN])))
    
#     return round(calculate_f1(TN,TP,FN,FP), 2)

# def evaluate_prominence(preds_dict: Dict, mode: str = "jaccard") -> float:
#     hits = 0
#     misses = 0

#     for article in preds_dict.values():
#         for preds in article.values():
#             if preds['prominence_rank'] == 1:
#                 if preds['prominent'] == 1:
#                     hits +=1
#                 else:
#                     misses += 1
#             else:
#                 pass

#     return round(hits / (hits + misses), 2)


# def plot_results(optimizer):
#     print(
#         "Best result: {}; f(x) = {:.3f}.".format(
#             optimizer.max["params"], optimizer.max["target"]
#         )
#     )

#     plt.figure(figsize=(15, 5))
#     plt.plot(range(1, 1 + len(optimizer.space.target)), optimizer.space.target, "-o")
#     plt.grid(True)
#     plt.xlabel("Iteration", fontsize=14)
#     plt.ylabel("Black box function f(x)", fontsize=14)
#     plt.xticks(fontsize=14)
#     plt.yticks(fontsize=14)
#     plt.show()


# def train_fuzzy():
#     def black_box_function(cutoff: int, scorer):
#         preds_dict = process_dataset(train, cutoff=cutoff, scorer=scorer)
#         accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)
#         return accuracy

#     pbounds = {"cutoff": [0, 100], "scorer": [0, len(FUZZUP_SCORERS) - 1]}

#     optimizer = BayesianOptimization(
#         f=black_box_function, pbounds=pbounds, verbose=2, random_state=4
#     )

#     utility = UtilityFunction(kind="ucb", kappa=1.96, xi=0.01)

#     # TRAINING LOOP
#     for i in range(25):
#         next_point = optimizer.suggest(utility)

#         next_point["scorer"] = int(next_point["scorer"])

#         target = black_box_function(
#             cutoff=next_point["cutoff"], scorer=next_point["scorer"]
#         )

#         try:
#             optimizer.register(params=next_point, target=target)
#         except:
#             pass
#         print(f"TARGET: {target} \n")
#         print(
#             f'cutoff: {next_point["cutoff"]} \n  scorer: {FUZZUP_SCORERS[next_point["scorer"]]} '
#         )

#     plot_results(optimizer)

# """
# Do not set weight_multipliers to 0, as all entities will get equal prominence_rank..
 
# Best result: {'weight_pos': 1.0, 'wgt_body': 3.0, 'wgt_lead': 7.4118645551409585, 'wgt_title': 3.0}; f(x) = 0.820.
# 'Best result: {'weight_pos': 0.0, 'wgt_body': 3.1199637756796292, 'wgt_lead': 11.1561038148714, 'wgt_title': 10.233392309970549}; f(x) = 0.840.
# """
# def train_prominent():
#     # prominence
#     def black_box_function(weight_pos: float, **kwargs):
#         preds_dict = process_dataset(
#             train, cutoff=96.703, scorer=1, weight_pos=weight_pos,
#             placement_col = 'text_segment', **kwargs
#         )
        
#         accuracy = evaluate_prominence2(preds_dict)
#         return accuracy

#     pbounds = {"weight_pos": [0,1],
#                "wgt_body": [0,20],
#                "wgt_lead": [0, 20],
#                "wgt_title": [0, 20],
#                }

#     optimizer = BayesianOptimization(
#         f=black_box_function, pbounds=pbounds, verbose=2, random_state=4
#     )

#     utility = UtilityFunction(kind="ucb", kappa=1.96, xi=0.01)

#     # TRAINING LOOP
#     for i in range(100):
#         next_point = optimizer.suggest(utility)

#         target = black_box_function(weight_pos=next_point['weight_pos'], wgt_body = next_point['wgt_body'], wgt_lead = next_point['wgt_lead'], wgt_title = next_point['wgt_title'])

#         try:
#             optimizer.register(params=next_point, target=target)
#         except:
#             pass
#         print(f"TARGET: {target} \n")
#         print(f'Weight_pos: {next_point["weight_pos"]} \n' )
#         print(f'wgt_body: {next_point["wgt_body"]} \n')
#         print(f'wgt_lead: {next_point["wgt_lead"]} \n')
#         print(f'wgt_title: {next_point["wgt_title"]} \n')
        
#     plot_results(optimizer)
    
# train = load_dataframe()

# train_prominent()

# # preds_dict = process_dataset(train, cutoff = 0, scorer=ratio)
# # accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)

# # print(f'ACCURACY: {accuracy} \n')
# # print(f'Number of articles with incorrect predictions: {len(diagnosis_dict)}')


# # optimizer.maximize()
# # print("Best result: {}; f(x) = {}.".format(optimizer.max["params"], optimizer.max["target"]))

# # __import__('pdb').set_trace()
