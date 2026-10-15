from cost_xray import verify


def test_iterator_aggregation_matches_list():
    reports = [
        {
            "reconstruction": {"input_err": 0.2, "output_err": 0.3},
            "coverage": {
                "ok": True,
                "missing": [],
                "orphan": [],
                "token_exact_delta": 0,
                "unknown_types": [],
            },
        }
    ]
    assert verify.aggregate(iter(reports)) == verify.aggregate(reports)
