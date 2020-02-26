from exercicios.exercicio_2 import formata_nome

print('''
Este programa formata o nome das pessoas com todas as iniciais maiúsculas
(nome, sobrenome, nome do meio com exceção do “de” ou “da”) ex.: José da Silva.
''')
print('Entre com o seu nome completo:')
nome_completo = input()
print('Resultado: ')
print(formata_nome(nome_completo))