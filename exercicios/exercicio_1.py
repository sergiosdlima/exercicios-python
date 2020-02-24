def calcula_imc(peso, altura):
    try:
        imc = peso / (altura * altura)
        if imc < 16:
            return 'Magreza grave'
        elif imc < 17:
            return 'Magreza moderada'
        elif imc < 18.5:
            return 'Magreza leve'
        elif imc < 25:
            return 'Saudável'
        elif imc < 30:
            return 'Sobrepeso'
        elif imc < 35:
            return 'Obesidade Grau I'
        elif imc < 40:
            return 'Obesidade Grau II (severa)'
        else:
            return 'Obesidade Grau III (mórbida)'
    except:
        return 'Valor inválido'


class TestClass:
    def test_valor_zero(self):
        assert calcula_imc(0, 0) == 'Valor inválido'

    def test_imc_menor_que_16(self):
        assert calcula_imc(35, 1.60) == 'Magreza grave'

    def test_imc_igual_16(self):
        assert calcula_imc(46.24, 1.70) == 'Magreza moderada'

    def test_imc_menor_que_17(self):
        assert calcula_imc(48, 1.70) == 'Magreza moderada'

    def test_imc_igual_17(self):
        assert calcula_imc(62.02, 1.91) == 'Magreza leve'

    def test_imc_igual_18(self):
        assert calcula_imc(65.66, 1.91) == 'Magreza leve'

    def test_imc_menor_que_18(self):
        assert calcula_imc(67.3, 1.91) == 'Magreza leve'

    def test_imc_igual_18_5(self):
        assert calcula_imc(67.5, 1.91) == 'Saudável'

    def test_imc_menor_que_25(self):
        assert calcula_imc(90, 1.91) == 'Saudável'

    def test_imc_igual_25(self):
        assert calcula_imc(91.3, 1.91) == 'Sobrepeso'

    def test_imc_menor_que_30(self):
        assert calcula_imc(105, 1.91) == 'Sobrepeso'

    def test_imc_igual_30(self):
        assert calcula_imc(109.5, 1.91) == 'Obesidade Grau I'

    def test_imc_menor_que_35(self):
        assert calcula_imc(125, 1.91) == 'Obesidade Grau I'

    def test_imc_igual_35(self):
        assert calcula_imc(127.7, 1.91) == 'Obesidade Grau II (severa)'

    def test_imc_menor_que_40(self):
        assert calcula_imc(145, 1.91) == 'Obesidade Grau II (severa)'

    def test_imc_igual_40(self):
        assert calcula_imc(145.93, 1.91) == 'Obesidade Grau III (mórbida)'

    def test_imc_maior_que_40(self):
        assert calcula_imc(150, 1.91) == 'Obesidade Grau III (mórbida)'