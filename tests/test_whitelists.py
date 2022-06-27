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
from fuzzup.fuzz import fuzzy_cluster, fuzzy_cluster_bygroup

c = EBLocalNames()
m = Municipalities()
n = Companies()


def test_whitelist():
    test_data = [
        {"word": "Viborg", "entity_group": "LOC", "cluster_id": "ABE"},
        {"word": "Uldum", "entity_group": "ORG", "cluster_id": "bambolino"},
    ]
    clusters = fuzzy_cluster(test_data)
    out = c(clusters, aggregate_cluster=False)
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
    out = apply_whitelists([c, m, n], clusters, score_cutoff=90)

    #### Format output
    # set desired columnsmunicipality_id
    cols = ["type", "id", "label"]

    # format output
    out = format_output(out, columns=cols, drop_duplicates=True)

    assert isinstance(out, pd.DataFrame)
    assert len(out) > 0
    "Frederiksberg" in dict(out["label"]).values()


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
    cols = ["type", "id", "label"]

    # format output
    out = format_output(test_data, columns=cols, drop_duplicates=True)
    assert isinstance(out, pd.DataFrame)
    assert len(out) > 0


def test_EBLocalNames():
    EBLocalNames()
