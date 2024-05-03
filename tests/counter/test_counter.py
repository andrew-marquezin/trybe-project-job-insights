from src.pre_built.counter import count_ocurrences


path = "data/jobs.csv"
word = "Python"


def test_counter():
    '''testa a execução da função "count_ocurrences"'''
    counter = count_ocurrences(path, word)
    assert counter == 1639
