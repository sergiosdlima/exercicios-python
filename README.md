# Curso de python3

Este repositório contém a resolução dos exercícios propostos no curso de python 3 gratuito da Udemy (Python 3 na Prática).

Lista de exercícios:

1. Calculadora de Índice de Massa Corporal (IMC). Para executar o programa, digite `python calculadora-imc.py` no terminal.

2. Formata o nome das pessoas com todas as iniciais maiúsculas (nome, sobrenome, nome do meio com exceção do “de” ou “da”) ex.: José da Silva.

## Setup

Usei o virtualenv para criar um ambiente isolado para rodar os exercícios e testes.

Comando utilizado para criar o ambiente no projeto:

`virtualenv --python=python3 vpy3`

Depois para ativar o ambiente:

`source ./vpy3/bin/activate`

Depois, instale a biblioteca pytest para testar o código dos exercícios:

`pip install pytest`

Para rodar os testes, execute o comando:

`pytest -v exercicios/*`