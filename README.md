# Curso de python3

Este repositório contém a resolução dos exercícios propostos no curso de python 3 gratuito da Udemy (Python 3 na Prática).

Usei o virtualenv para criar um ambiente isolado para rodar os exercícios e testes.

Comando utilizado para criar o ambiente no projeto:

`virtualenv --python=python3 vpy3`

Depois para ativar o ambiente:

`source ./vpy3/bin/activate`

Depois, instale a biblioteca pytest para testar o código dos exercícios:

`pip install pytest`

Para rodar os testes, execute o comando:

`pytest -v exercicios/*`