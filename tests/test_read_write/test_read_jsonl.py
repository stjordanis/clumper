import pytest
from clumper import Clumper


@pytest.mark.parametrize("lines, expected", [(None, 4), (0, 0), (1, 1), (2, 2), (5, 4)])
def test_local_read_jsonl_expected(single_local_jsonl_file_path, lines, expected):
    assert (
        len(Clumper.read_jsonl(single_local_jsonl_file_path, lines)) == expected
    ), "The number of lines read is not equal to expected number of lines"


@pytest.mark.parametrize(
    "lines, expected", [(None, 800), (0, 0), (1, 1), (2, 2), (801, 800)]
)
def test_cloud_read_jsonl_expected(single_cloud_jsonl_file_path, lines, expected):
    assert (
        len(Clumper.read_jsonl(single_cloud_jsonl_file_path, lines)) == expected
    ), "The number of lines read is not equal to expected number of lines"
