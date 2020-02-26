def formata_nome(nome_completo):
    lista_nome_capitalizado = [nome.capitalize() for nome in nome_completo.split()]
    nome_formatado = ' '.join(lista_nome_capitalizado)
    nome_formatado = nome_formatado.replace(' Da ', ' da ').replace(' De ', ' de ')
    return nome_formatado


class TestCase:
    def test_nome_simples(self):
        assert formata_nome('marina') == 'Marina'

    def test_nome_sobrenome_simples(self):
        assert formata_nome('marina matos') == 'Marina Matos'

    def test_sobrenome_com_de(self):
        assert formata_nome('marina de matos') == 'Marina de Matos'

    def test_sobrenome_com_da(self):
        assert formata_nome('paulo da silva') == 'Paulo da Silva'

    def test_nome_com_acento_sobrenome_com_da(self):
        assert formata_nome('áida da silva') == 'Áida da Silva'

    def test_nome_completo(self):
        assert formata_nome('sérgio santana de lima') == 'Sérgio Santana de Lima'

    def test_nome_sobrenome_caixa_alta(self):
        assert formata_nome('SÉRGIO SANTANA DE LIMA') == 'Sérgio Santana de Lima'

    def test_nome_vazio(self):
        assert formata_nome('') == ''
