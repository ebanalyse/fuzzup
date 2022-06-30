from multiprocessing.sharedctypes import Value
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
from typing import List, Dict, Callable
import numpy as np
from fuzzup.fuzz import (
    fuzzy_cluster_bygroup,
    fuzzy_cluster,
    compute_prominence_bygroup,
    compute_prominence_placement,
)
from fuzzup.whitelists import EBLocalNames, Municipalities, Companies, apply_whitelists
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
import matplotlib.pyplot as plt

from bayes_opt import BayesianOptimization, UtilityFunction

import json

import ast

FUZZUP_SCORERS = {
    0: ratio,
    1: partial_ratio,
    2: partial_token_set_ratio,
    3: WRatio,
    4: QRatio,
    5: token_set_ratio,
}

WHITELISTS = [EBLocalNames(), Municipalities(), Companies()]

train = pd.read_excel("./processed_annotated_dump.xlsx")

train = train[train["entity_group"] == "LOC"]


def _assert_fuzz_json(json_data):
    if not all(key in json_data for key in ("title", "body")):
        raise ValueError("One of title or body not found in request")

    if "lead" not in json_data or type(json_data["lead"]) is not str:
        json_data["lead"] = ""  # Can be empty since not all articles have one

    if "sentence_based" not in json_data:
        json_data["sentence_based"] = True

    return json_data


def _text_segment_adder(json_data, preds_out):
    # This will probably require that each piece of text is seperated by a \n
    for pred in preds_out:
        lens = [len(json_data["title"]), len(json_data["lead"]), len(json_data["body"])]
        if pred["start"] <= lens[0]:
            pred["text_segment"] = "title"
        elif pred["start"] <= lens[0] + lens[1]:
            pred["text_segment"] = "lead"
        elif pred["start"] <= lens[0] + lens[1] + lens[2]:
            pred["text_segment"] = "body"
        else:
            pred["text_segment"] = "body"
    return preds_out


def flatten_whitelist(wl_clusters) -> List:
    match_city = []
    match_municipality = []

    if (
        len(wl_clusters["eblocal_name"]) > 0
        or len(wl_clusters["municipality"]) > 0
        or len(wl_clusters["company"]) > 0
    ):
        for whitelist in wl_clusters:
            for matches in wl_clusters[whitelist]:
                match = matches["matches"]
                for mapping in matches["mappings"]:
                    if whitelist == "eblocal_name" or whitelist == "company":
                        if (match, mapping["label"]) not in match_city:
                            match_city.append((match, mapping["type"]))
    return match_city


def _predict(
    preds: List[Dict],
    # cutoff_fuzz,
    cutoff_wl,
    # scorer_fuzz,
    scorer_wl,
    wgt_body,
    wgt_lead,
    wgt_title,
    weight_pos,
    json_data,
) -> Dict:
    res = defaultdict(lambda: {})

    json_data = _assert_fuzz_json(json_data)
    fuzzy_preds = fuzzy_cluster_bygroup(preds, cutoff=96.7, scorer=token_ratio)

    fuzzy_preds = _text_segment_adder(json_data, fuzzy_preds)

    try:
        fuzzy_preds = compute_prominence_placement(
            fuzzy_preds,
            placement_col="text_segment",
            weight_position=weight_pos,
            wgt_lead=wgt_lead,
            wgt_body=wgt_body,
            wgt_title=wgt_title,
            return_first_rank=True,
            bygroup=True,
        )
    except:
        __import__("pdb").set_trace()

    whitelist_matches = apply_whitelists(
        WHITELISTS,
        fuzzy_preds,
        scorer=FUZZUP_SCORERS[scorer_wl],
        score_cutoff=cutoff_wl,
        aggregate_cluster=True,
        match_strategy=False,
    )

    match_city = flatten_whitelist(whitelist_matches)

    """
    TODO:  if fuzzy_pred returns an empty dictionary, then the evaluation goes wrong, as true_value will never be appended either?
    """

    for i, fuzzy_pred in enumerate(fuzzy_preds):
        #   #  Filter any predictions with a score of lower than 10
        #     if fuzzy_pred['prominence_score'] >= 10:
        #         continue
        #     elif fuzzy_pred['prominence_rank'] != 1 and fuzzy_pred['prominence_score'] <10:
        #         #If the score is lower than 10, then the prediction is nothing
        #         match_city = []
        res[i].update(
            {
                "word": fuzzy_pred["word"],
                "pred": match_city,
                "true_value": fuzzy_pred["true_value"],
                "prominence_rank": fuzzy_pred["prominence_rank"],
                "prominence_score": fuzzy_pred["prominence_score"],
            }
        )
    i = 0
    if len(res) == 0:
        res[i].update(
            {
                "word": fuzzy_pred["word"],
                "pred": match_city,
                "true_value": fuzzy_pred["true_value"],
                "prominence_rank": fuzzy_pred["prominence_rank"],
                "prominence_score": fuzzy_pred["prominence_score"],
            }
        )
        i += 1

    return res


def process_dataset(
    train: pd.DataFrame,  # cutoff_fuzz,
    cutoff_wl,
    #    scorer_fuzz,
    scorer_wl,
    wgt_body,
    wgt_lead,
    wgt_title,
    weight_pos,
) -> List[Dict]:

    if "subtitle" in train:
        train = train.rename({"subtitle": "lead"}, axis="columns")
    if "body_text" in train:
        train = train.rename({"body_text": "body"}, axis="columns")
    if "article_id" in train:
        train = train.rename({"article_id": "content_id"}, axis="columns")

    preds_dict = defaultdict(lambda: {})
    with tqdm(total=train["content_id"].nunique()) as pbar:
        for article in np.unique(train["content_id"]):
            pbar.update(1)
            preds_list = []
            json_data = {}
            for index, row in train[train["content_id"] == article].iterrows():
                row["true_value"] = ast.literal_eval(row["NER-matches_city"])
                preds_list.append(dict(row))
            json_data["title"] = row["title"]
            json_data["body"] = row["body"]
            if "lead" in row is not None:
                json_data["lead"] = row["lead"]
            preds_dict[article].update(
                _predict(
                    preds_list,
                    #   cutoff_fuzz,
                    cutoff_wl,
                    #   scorer_fuzz,
                    scorer_wl,
                    wgt_body,
                    wgt_lead,
                    wgt_title,
                    weight_pos,
                    json_data,
                )
            )
    return preds_dict


def clean_preds(preds: Dict) -> Dict:
    clean_preds = []
    clean_true = []

    if len(preds["pred"]) > 0:
        for pred in preds["pred"]:
            for entry in pred[0]:
                clean_preds.append(entry)
    if len(preds["true_value"]) > 0:
        for pred in preds["true_value"]:
            for entry in pred[0]:
                clean_true.append(entry)

    preds["pred"] = clean_preds
    preds["true_value"] = clean_true
    return preds


def evaluate_whitelist_matching(preds_dict: Dict, mode: str = "jaccard") -> float:
    TN = 0
    TP = 0
    FN = 0
    FP = 0

    if mode == "f1":
        pass

    if mode == "jaccard":
        accuracies = {}
        diagnosis_dict = {}
        for article in preds_dict.keys():
            preds_set = set()
            true_set = set()
            for preds in preds_dict[article].values():
                preds = clean_preds(preds)
                for pred in preds["pred"]:
                    preds_set.add(pred)
                for true_val in preds["true_value"]:
                    true_set.add(true_val)

            if len(preds_set) != 0 and len(true_set) != 0:
                accuracy = round(
                    len(preds_set.intersection(true_set))
                    / len(preds_set.union(true_set)),
                    2,
                )
                if len(preds_set - true_set) != 0:
                    diagnosis_dict[article] = {
                        "preds_set": preds_set,
                        "true_set": true_set,
                        "misses": preds_set - true_set,
                    }
                print("predictions: ", preds_set, "true_value: ", true_set)
            elif len(preds_set) == 0 and len(true_set) == 0:
                pass
            elif len(preds_set) and not len(true_set):
                accuracy = 0
            elif not len(preds_set) and len(true_set):
                accuracy = 0
            else:
                accuracy = 0

            try:
                accuracies[article] = accuracy
            except:
                continue
        if len(accuracies) != 0:
            return (
                sum(accuracies.values()) / len(accuracies),
                diagnosis_dict,
            )  # Return the mean accurac
        else:
            return 0, None


def evaluate_fuzzy_matching(preds_dict: Dict, mode: str = "jaccard") -> float:
    """Just loops through the preds dict and aggregates their evaluations"""

    if mode == "jaccard":
        accuracies = {}
        diagnosis_dict = {}
        for article in preds_dict.keys():
            preds_set = set()
            true_set = set()
            for preds in preds_dict[article].values():
                preds_set.add(preds["pred"].lower())
                true_set.add(preds["true_value"].lower())
            if len(preds_set) != 0 and len(true_set) != 0:
                accuracy = round(
                    len(preds_set.intersection(true_set))
                    / len(preds_set.union(true_set)),
                    2,
                )
                if len(preds_set - true_set) != 0:
                    diagnosis_dict[article] = {
                        "preds_set": preds_set,
                        "true_set": true_set,
                        "misses": preds_set - true_set,
                    }
            else:
                pass
            accuracies[article] = accuracy
        return (
            sum(accuracies.values()) / len(accuracies),
            diagnosis_dict,
        )  # Return the mean accuracy of all jaccard indices

    elif mode == "dice":
        res = {}

        for article in preds_dict.values():
            pred_set = set()
            true_set = set()
            for preds in article.values():
                if preds["pred"] not in pred_set:
                    pred_set.add(preds["pred"])
                if preds["true_value"] not in true_set:
                    true_set.add(preds["true_value"])
            dice_similarity = (2 * len(np.intersect1d(pred_set, true_set))) / (
                len(pred_set) ** 2 + len(true_set) ** 2
            )

    else:
        raise ValueError('Please set mode arg to either "jaccard" or "dice"')


def calculate_f1(TN: float, TP: float, FN: float, FP: float) -> float:
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * (precision * recall) / (precision + recall)
    return f1


def evaluate_prominence2(preds_dict: Dict, mode: str = "jaccard") -> float:
    TN = 0
    TP = 0
    FN = 0
    FP = 0
    # 2 * (Precision * Recall) / (Precision + Recall)
    for article in preds_dict.values():
        for preds in article.values():
            if preds["prominence_score"] >= 10:
                if preds["prominent"] == 1:
                    TP += 1
                else:
                    FP += 1
            if preds["prominence_score"] < 10:
                if preds["prominent"] == 0:
                    TN += 1
                else:
                    FN += 1

    print("CONFUSION MATRIX: \n")
    print(np.array(([TP, FP], [FN, TN])))

    return round(calculate_f1(TN, TP, FN, FP), 2)


def evaluate_prominence(preds_dict: Dict, mode: str = "jaccard") -> float:
    hits = 0
    misses = 0

    for article in preds_dict.values():
        for preds in article.values():
            if preds["prominence_rank"] == 1:
                if preds["prominent"] == 1:
                    hits += 1
                else:
                    misses += 1
            else:
                pass

    return round(hits / (hits + misses), 2)


def plot_results(optimizer):
    print(
        "Best result: {}; f(x) = {:.3f}.".format(
            optimizer.max["params"], optimizer.max["target"]
        )
    )

    plt.figure(figsize=(15, 5))
    plt.plot(range(1, 1 + len(optimizer.space.target)), optimizer.space.target, "-o")
    plt.grid(True)
    plt.xlabel("Iteration", fontsize=14)
    plt.ylabel("Black box function f(x)", fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()


def train_whitelist():
    def black_box_function(**kwargs):
        preds_dict = process_dataset(train, **kwargs)
        accuracy, diagnosis_dict = evaluate_whitelist_matching(preds_dict)
        return accuracy

    pbounds = {  # "cutoff_fuzz": [0, 100],
        "cutoff_wl": [80, 100],
        # "scorer_fuzz": [0, len(FUZZUP_SCORERS) - 1],
        "scorer_wl": [0, len(FUZZUP_SCORERS) - 1],
        "weight_pos": [0.99, 1],
        "wgt_body": [0.99, 1],
        "wgt_lead": [0.99, 1],
        "wgt_title": [0.99, 1],
    }

    optimizer = BayesianOptimization(
        f=black_box_function, pbounds=pbounds, verbose=2, random_state=4
    )

    utility = UtilityFunction(kind="ucb", kappa=1.96, xi=0.01)

    # TRAINING LOOP
    for i in range(200):
        next_point = optimizer.suggest(utility)

        target = black_box_function(
            # cutoff_fuzz=next_point["cutoff_fuzz"],
            # scorer_fuzz=int(next_point["scorer_fuzz"]),
            cutoff_wl=next_point["cutoff_wl"],
            scorer_wl=int(next_point["scorer_wl"]),
            weight_pos=next_point["weight_pos"],
            wgt_body=next_point["wgt_body"],
            wgt_lead=next_point["wgt_lead"],
            wgt_title=next_point["wgt_title"],
        )

        try:
            optimizer.register(params=next_point, target=target)
        except:
            pass
        print(f"TARGET: {target} \n")
        print(next_point)

    plot_results(optimizer)

    pass


def train_fuzzy():
    def black_box_function(cutoff: int, scorer):
        preds_dict = process_dataset(train, cutoff=cutoff, scorer=scorer)
        accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)
        return accuracy

    pbounds = {"cutoff": [0, 100], "scorer": [0, len(FUZZUP_SCORERS) - 1]}

    optimizer = BayesianOptimization(
        f=black_box_function, pbounds=pbounds, verbose=2, random_state=4
    )

    utility = UtilityFunction(kind="ucb", kappa=1.96, xi=0.01)

    # TRAINING LOOP
    for i in range(25):
        next_point = optimizer.suggest(utility)

        next_point["scorer"] = int(next_point["scorer"])

        target = black_box_function(
            cutoff=next_point["cutoff"], scorer=next_point["scorer"]
        )

        try:
            optimizer.register(params=next_point, target=target)
        except:
            pass
        print(f"TARGET: {target} \n")
        print(
            f'cutoff: {next_point["cutoff"]} \n  scorer: {FUZZUP_SCORERS[next_point["scorer"]]} '
        )

    plot_results(optimizer)


"""
Do not set weight_multipliers to 0, as all entities will get equal prominence_rank..
 
Best result: {'weight_pos': 1.0, 'wgt_body': 3.0, 'wgt_lead': 7.4118645551409585, 'wgt_title': 3.0}; f(x) = 0.820.
'Best result: {'weight_pos': 0.0, 'wgt_body': 3.1199637756796292, 'wgt_lead': 11.1561038148714, 'wgt_title': 10.233392309970549}; f(x) = 0.840.
Best result: {'cutoff_wl': 92.37154146074903, 'scorer_wl': 0.0, 'weight_pos': 1.0, 'wgt_body': 0.99, 'wgt_lead': 10.0, 'wgt_title': 10.0}; f(x) = 0.456.
Best result: {'cutoff_wl': 91.98047495901676, 'scorer_wl': 0.43219773246841736, 'weight_pos': 1.0, 'wgt_body': 0.99, 'wgt_lead': 1.86707316458525, 'wgt_title': 2.029549572307997}; f(x) = 0.572.
"""


def train_prominent():
    # prominence
    def black_box_function(weight_pos: float, **kwargs):
        preds_dict = process_dataset(
            train,
            cutoff=96.703,
            scorer=1,
            weight_pos=weight_pos,
            placement_col="text_segment",
            **kwargs,
        )

        accuracy = evaluate_prominence2(preds_dict)
        return accuracy

    pbounds = {
        "weight_pos": [0, 1],
        "wgt_body": [0, 20],
        "wgt_lead": [0, 20],
        "wgt_title": [0, 20],
    }

    optimizer = BayesianOptimization(
        f=black_box_function, pbounds=pbounds, verbose=2, random_state=4
    )

    utility = UtilityFunction(kind="ucb", kappa=1.96, xi=0.01)

    # TRAINING LOOP
    for i in range(100):
        next_point = optimizer.suggest(utility)

        target = black_box_function(
            weight_pos=next_point["weight_pos"],
            wgt_body=next_point["wgt_body"],
            wgt_lead=next_point["wgt_lead"],
            wgt_title=next_point["wgt_title"],
        )

        try:
            optimizer.register(params=next_point, target=target)
        except:
            pass
        print(f"TARGET: {target} \n")
        print(f'Weight_pos: {next_point["weight_pos"]} \n')
        print(f'wgt_body: {next_point["wgt_body"]} \n')
        print(f'wgt_lead: {next_point["wgt_lead"]} \n')
        print(f'wgt_title: {next_point["wgt_title"]} \n')

    plot_results(optimizer)


def single_run(**kwargs):
    preds_dict = process_dataset(train, **kwargs)
    accuracy, diagnosis_dict = evaluate_whitelist_matching(preds_dict)
    print(accuracy)
    __import__("pdb").set_trace()


# Best result: {'cutoff_wl': 92.37154146074903, 'scorer_wl': 0.0, 'weight_pos': 1.0, 'wgt_body': 0.99, 'wgt_lead': 10.0, 'wgt_title': 10.0}; f(x) = 0.456.

single_run(
    # cutoff_fuzz=next_point["cutoff_fuzz"],
    # scorer_fuzz=int(next_point["scorer_fuzz"]),
    # cutoff_fuzz=97,
    # scorer_fuzz=token_ratio,
    cutoff_wl=98.0,
    scorer_wl=3,
    weight_pos=1,
    wgt_body=1,
    wgt_lead=1,
    wgt_title=1,
)

# train_whitelist()

# preds_dict = process_dataset(train, cutoff = 0, scorer=ratio)
# accuracy, diagnosis_dict = evaluate_fuzzy_matching(preds_dict)

# print(f'ACCURACY: {accuracy} \n')
# print(f'Number of articles with incorrect predictions: {len(diagnosis_dict)}')


# optimizer.maximize()
# print("Best result: {}; f(x) = {}.".format(optimizer.max["params"], optimizer.max["target"]))

# __import__('pdb').set_trace()
