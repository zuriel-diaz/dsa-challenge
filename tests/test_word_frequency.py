from dsa_pennymac.word_frequency import solution

TARGET_WORD = "PENNYMAC"


def test_empty_list():
    assert solution(TARGET_WORD, []) == 0


def test_empty_str():
    assert solution(TARGET_WORD, "") == 0


def test_missing_letters():
    assert solution(TARGET_WORD, ["P", "N", "N", "Y", "M", "A", "C"]) == 0


def test_single_occurrence():
    assert solution(TARGET_WORD, ["P", "E", "N", "N", "Y", "M", "A", "C"]) == 1


def test_multiple_occurrences():
    pass
