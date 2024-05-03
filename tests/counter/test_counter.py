from src.pre_built.counter import count_ocurrences


path = "data/jobs.csv"


def test_counter():
    '''testa a execução da função "count_ocurrences"'''
    python_counter = count_ocurrences(path, "python")
    js_counter = count_ocurrences(path, "javascript")
    assert python_counter == 1639
    assert js_counter == 122
