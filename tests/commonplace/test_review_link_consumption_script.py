from scripts.review_link_consumption import _offered_count


def test_offered_count_supports_known_schemas_and_rejects_invalid_counts() -> None:
    offered = {
        "distinct_link_target_count": 3,
        "distinct_consumption_target_count": 5,
        "distinct_artifact_count": 9,
    }

    assert _offered_count(3, offered) == 5
    assert _offered_count(2, {"distinct_artifact_count": 4}) == 4
    assert _offered_count(1, {"distinct_artifact_count": 4}) == 4
    assert _offered_count(4, {"distinct_consumption_target_count": 3}) is None
    assert _offered_count(3, {"distinct_consumption_target_count": True}) is None
    assert _offered_count(3, {"distinct_consumption_target_count": -1}) is None
