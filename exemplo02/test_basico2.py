def somar(a,b):
    return a + b

def test_somar():
    assert somar(2,3) == 5

def comprimento(lista):
    return len(lista)

def test_comprimento():
    assert comprimento([2,3,4,5,6,7]) == 6

def test_comprimento_e_somar():
    assert comprimento([2,3,4,5,6,7]) == 6
    assert somar(2,3) == 5



