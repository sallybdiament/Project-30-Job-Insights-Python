from src.pre_built.counter import count_ocurrences


mock_text = "contar quantas vezes aparece python neste texto. Python"
file_path = "src/fake_file_path"


def test_counter():
    result = count_ocurrences("data/jobs.csv", "marketing")
    assert result == 1259
