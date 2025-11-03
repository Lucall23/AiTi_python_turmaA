from funcoes import *

def test_email_valido():
    assert email_valido("lr6056682@gmail.com") is True
    assert email_valido("gmail.com") is False

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None
