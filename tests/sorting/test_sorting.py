from src.pre_built.sorting import sort_by
import pytest


error_msg = "invalid sorting criteria: not_valid"
jobs = [
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
    ]


def test_sort_by_criteria():
    with pytest.raises(KeyError, match=error_msg):
        sort_by(jobs, "not_valid")
