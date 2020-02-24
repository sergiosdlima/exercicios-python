from exercicios.exercicio_1 import *

print('''
IMC é a sigla para Índice de Massa Corporal que serve para avaliar o peso do
indivíduo em relação à sua altura e assim indicar se está dentro do peso ideal,
acima ou abaixo do peso desejado.
''')
print('Entre com o seu peso:')
peso = input()
print('Entre com a sua altura:')
altura = input()
imc = calcula_imc(float(peso), float(altura))
if imc == 'Valor inválido':
    print('Você informou valores inválidos. Tente novamente.')
else:
    print('O seu IMC indica que você está: ' + imc)