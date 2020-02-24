def formata_nome_completo(nome_completo):
    lista_nomes = nome_completo.split()
    for i, nome in enumerate(lista_nomes):
        if nome != 'de' and nome != 'da':
            lista_nomes[i] = nome.capitalize()

    return ' '.join(lista_nomes)

class TestCase:
    def test_nome_simples(self):
        assert formata_nome_completo('marina') == 'Marina'

    def test_nome_sobrenome_simples(self):
        assert formata_nome_completo('marina matos') == 'Marina Matos'

    def test_sobrenome_com_de(self):
        assert formata_nome_completo('marina de matos') == 'Marina de Matos'

    def test_sobrenome_com_da(self):
        assert formata_nome_completo('paulo da silva') == 'Paulo da Silva'

    def test_nome_com_acento_sobrenome_com_da(self):
        assert formata_nome_completo('áida da silva') == 'Áida da Silva'

    def test_nome_completo(self):
        assert formata_nome_completo('sérgio santana de lima') == 'Sérgio Santana de Lima'

    def test_nome_vazio(self):
        assert formata_nome_completo('') == ''
