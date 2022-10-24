from src.counter import count_ocurrences


def test_counter():
    'Se a função conta corretamente as palavras Python e JavaScript'
    assert count_ocurrences("src/jobs.csv", "Python") == 1639
    assert count_ocurrences("src/jobs.csv", "JavaScript") == 122
