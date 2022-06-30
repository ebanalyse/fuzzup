import pandas as pd

from fuzzup.whitelists import (
    match_whitelist,
    Cities,
    Municipalities,
    Neighborhoods,
    format_output,
    apply_whitelists,
    EBLocalNames,
    Companies,
)

from rapidfuzz.fuzz import WRatio, token_ratio

from fuzzup.fuzz import fuzzy_cluster, fuzzy_cluster_bygroup

c = EBLocalNames()
m = Municipalities()
n = Companies()

WHITELISTS = [c, m, n]


def test_whitelist():
    test_data = [
        {"word": "Viborg", "entity_group": "LOC", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters, aggregate_cluster=False, match_strategy=False)
    assert len(out) == 1


def test_whitelist_major_cities():
    test_data = [
        {"word": "København", "entity_group": "LOC", "cluster_id": "København"},
        {"word": "Aarhus V", "entity_group": "LOC", "cluster_id": "Aarhus Vest"},
        {"word": "Aarhus", "entity_group": "LOC", "cluster_id": "Aarhus"},
    ]
    clusters = fuzzy_cluster_bygroup(test_data)
    matches = apply_whitelists(whitelists=[c, m, n], clusters=clusters)
    copenhagen_bool = False
    aarhus_bool = False
    for label in matches["eblocal_name"]:
        matches = label["matches"]
        if "København K" in matches:
            copenhagen_bool = True
        if "Aarhus C" in matches:
            aarhus_bool = True
    assert copenhagen_bool and aarhus_bool


def test_match_strategy_weighting():
    """This test-case involves the situation, where you use match_strategy
    but prominence_ranks are not based on basic counts. Meaning, they have been
    linear interpolated or similar.
    regardless of the ranks, we still want the rank 2 entity to have appeared at least twice
    in this case when using match-strategy
    """
    test_data = [
        {
            "score": 0.9999998807907104,
            "word": "Limfjordstunnelen",
            "start": 17,
            "end": 34,
            "label": "LOC",
            "entity_group": "LOC",
            "cluster_id": "Limfjordstunnelen E45",
            "prominence_score": 2.9771830985915493,
            "prominence_rank": 1,
        },
        {
            "score": 0.9999991655349731,
            "word": "Limfjordstunnelen",
            "start": 85,
            "end": 102,
            "label": "LOC",
            "entity_group": "LOC",
            "cluster_id": "Limfjordstunnelen E45",
            "prominence_score": 2.9771830985915493,
            "prominence_rank": 1,
        },
        {
            "score": 0.9972279071807861,
            "word": "Limfjordstunnelen E45",
            "start": 192,
            "end": 213,
            "label": "LOC",
            "entity_group": "LOC",
            "cluster_id": "Limfjordstunnelen E45",
            "prominence_score": 2.9771830985915493,
            "prominence_rank": 1,
        },
        {
            "score": 1.0,
            "word": "Aalborg",
            "start": 218,
            "end": 225,
            "label": "LOC",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_score": 0.9811267605633802,
            "prominence_rank": 2,
        },
        {
            "score": 1.0,
            "word": "Nørresundby",
            "start": 230,
            "end": 241,
            "label": "LOC",
            "entity_group": "LOC",
            "cluster_id": "Nørresundby",
            "prominence_score": 0.98,
            "prominence_rank": 3,
        },
        {
            "score": 1.0,
            "word": "Nordjyllands Politi",
            "start": 347,
            "end": 366,
            "label": "ORG",
            "entity_group": "ORG",
            "cluster_id": "Nordjyllands Politi",
            "prominence_score": 1.0,
            "prominence_rank": 1,
        },
        {
            "score": 0.9999994039535522,
            "word": "Twitter",
            "start": 370,
            "end": 377,
            "label": "ORG",
            "entity_group": "ORG",
            "cluster_id": "Twitter",
            "prominence_score": 0.98,
            "prominence_rank": 2,
        },
    ]
    whitelist_clusters = apply_whitelists(
        whitelists=WHITELISTS,
        clusters=test_data,
        score_cutoff=97,
        scorer=WRatio,
        aggregate_cluster=True,
        match_strategy=True,
    )
    for key, val in whitelist_clusters.items():
        assert not len(val)  # make sure all values are empty


def test_whitelist_match_strategy_rank_2():

    test_data = [
        {
            "word": "Volapyk",
            "entity_group": "LOC",
            "cluster_id": "Volapyk",
            "prominence_rank": 1,
        },
        {
            "word": "Volapyk",
            "entity_group": "LOC",
            "cluster_id": "Volapyk",
            "prominence_rank": 1,
        },
        {
            "word": "Volapyk",
            "entity_group": "LOC",
            "cluster_id": "Volapyk",
            "prominence_rank": 1,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
    ]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters, aggregate_cluster=False, match_strategy=True)

    # Assert that all outputs are of rank 2 and not 1 or 3
    for item in out:
        assert item["prominence_rank"] == 2 or item["prominence_rank"] == 1


def test_match_no_strategy_individual_wl():
    test_data = [
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
    ]
    clusters = fuzzy_cluster(test_data)

    out = c(
        clusters,
        aggregate_cluster=False,
        match_strategy=False,
        individual_wl_match=True,
    )


def test_match_strategy_rank_1():
    test_data = [
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Odense",
            "entity_group": "LOC",
            "cluster_id": "Odense",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
    ]
    clusters = fuzzy_cluster(test_data)

    out = c(clusters, aggregate_cluster=False, match_strategy=True)
    # with no match strategy, we wanna return as many entities as we passed the function
    for item in out:
        """Test that only rank 1 and 2 with counts greater or equal to 2 are
        returned when using match output"""
        assert (
            item["cluster_id"] == "København"
            or item["cluster_id"] == "Aarhus"
            or item["cluster_id"] == "Aalborg"
        )


def test_no_match_strategy():
    test_data = [
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "København",
            "entity_group": "LOC",
            "cluster_id": "København",
            "prominence_rank": 1,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aarhus",
            "entity_group": "LOC",
            "cluster_id": "Aarhus C",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Aalborg",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Aalborg",
            "prominence_rank": 3,
        },
        {
            "word": "Volapyk",
            "entity_group": "LOC",
            "cluster_id": "Volapyk",
            "prominence_rank": 4,
        },
    ]
    clusters = fuzzy_cluster(test_data)

    out = c(clusters, aggregate_cluster=False, match_strategy=False)
    # with no match strategy, we wanna return as many entities as we passed the function
    assert len(clusters) == len(test_data)
    assert len(out) == len(test_data) - 1  # Except the entity that has no match


def test_whitelist_no_match():
    test_data = [
        {"word": "Viborg", "entity_group": "LO", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters)
    assert len(out) == 0


def test_whitelist_no_input():
    test_data = []
    clusters = fuzzy_cluster(test_data)
    out = c(clusters)
    assert len(out) == 0


def test_whitelist_list_input():
    test_data = [
        {"word": "Viborg", "entity_group": "LO", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    matches = match_whitelist(clusters, whitelist=["Viborg"])
    assert len(matches) == 1


def test_whitelist_aggregate_cluster():
    test_data = [
        {"word": "Viborg", "entity_group": "LOC", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters, aggregate_cluster=True)
    assert len(out) == 1


def test_municipalities_whitelist():
    test_data = [
        {"word": "Viborg Kommune", "entity_group": "LOC", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    out = m(clusters, score_cutoff=95)
    assert len(out) > 0


def test_whitelist_formatting():
    # simulate data
    test_data = [
        {"word": "Holbæk", "entity_group": "LOC", "cluster_id": "Holbæk"},
        {"word": "Holbæk", "entity_group": "ORG", "cluster_id": "Holbæk"},
        {
            "word": "Holbæk Kommune",
            "entity_group": "LOC",
            "cluster_id": "Holbæk Kommune",
        },
        {
            "word": "Frederiksberg Centret",
            "entity_group": "ORG",
            "cluster_id": "Frederiksberg Centret",
        },
    ]
    clusters = fuzzy_cluster(test_data)

    # Apply multiple whitelists
    out = apply_whitelists([c, m, n], clusters, score_cutoff=90, match_strategy=True)

    #### Format output
    # set desired columnsmunicipality_id
    cols = ["type", "id", "label", "version"]

    # format output
    out = format_output(out, columns=cols, drop_duplicates=True)
    assert isinstance(out, pd.DataFrame)
    assert len(out) > 0
    "Frederiksberg" in dict(out["label"]).values()


def test_whitelist_formatting_match_strategy():
    # simulate data
    test_data = [
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Holbæk",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk",
            "entity_group": "LOC",
            "cluster_id": "Holbæk",
            "prominence_rank": 2,
        },
        {
            "word": "Holbæk Kommune",
            "entity_group": "LOC",
            "cluster_id": "Holbæk Kommune",
            "prominence_rank": 1,
        },
        {
            "word": "Københavns Kommune",
            "entity_group": "LOC",
            "cluster_id": "Københavns Kommune",
            "prominence_rank": 2,
        },
        {
            "word": "Frederiksberg Centret",
            "entity_group": "ORG",
            "cluster_id": "Frederiksberg Centret",
            "prominence_rank": 3,
        },
        {
            "word": "Frederiksberg Centret",
            "entity_group": "ORG",
            "cluster_id": "Frederiksberg Centret",
            "prominence_rank": 3,
        },
    ]
    clusters = fuzzy_cluster(test_data)

    # Apply multiple whitelists
    out = apply_whitelists([c, m, n], clusters, score_cutoff=90, match_strategy=True)

    #### Format output
    # set desired columnsmunicipality_id
    cols = ["type", "id", "label", "version"]

    # format output
    out = format_output(out, columns=cols, drop_duplicates=True)
    label_dict_values = dict(out["label"]).values()
    assert isinstance(out, pd.DataFrame)
    assert len(out) > 0
    assert "Frederiksberg" not in label_dict_values
    assert "Holbæk Kommune" in label_dict_values
    assert "Holbæk" in label_dict_values
    assert "København Kommune" not in label_dict_values


def test_format_no_match_on_subcategory():
    # simulate datamunicipality_id
    test_data = {
        "city": [
            {
                "word": "Viborg",
                "entity_group": "LOC",
                "cluster_id": "Viborg",
                "matches": ["Visborg", "Viborg"],
                "mappings": [
                    {
                        "municipality": ["Mariagerfjord"],
                        "city_code": "12337669-ca46-6b98-e053-d480220a5a3f",
                    },
                    {
                        "municipality": ["Viborg"],
                        "city_code": "12337669-ba55-6b98-e053-d480220a5a3f",
                    },
                ],
            }
        ],
        "municipality": [
            {
                "word": "Viborg",
                "entity_group": "LOC",
                "cluster_id": "Viborg",
                "matches": ["Viborg"],
                "mappings": [{"municipality_code": "0791"}],
            }
        ],
    }
    # NOTE: no Neighborhood Code match

    #### Format output
    # set desired columnsmunicipality_id
    cols = ["type", "id", "label", "version"]

    # format output
    out = format_output(test_data, columns=cols, drop_duplicates=True)
    assert isinstance(out, pd.DataFrame)
    assert len(out) > 0


def test_EBLocalNames():
    EBLocalNames()
