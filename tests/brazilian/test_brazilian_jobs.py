# import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file


expected_result = {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'}


def test_brazilian_jobs():
    result = read_brazilian_file(("tests/mocks/brazilians_jobs.csv"))
    assert result[0] == expected_result
