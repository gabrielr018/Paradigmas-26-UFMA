# Cadastro de Pacientes e Cálculo de IMC — POO

# 

# Projeto acadêmico desenvolvido em Python para cadastro de pacientes, cálculo do Índice de Massa Corporal (IMC) e classificação do resultado.

# 

# O projeto foi refatorado utilizando Programação Orientada a Objetos (POO), com o objetivo de organizar o código, separar responsabilidades e facilitar sua manutenção.

# 

# Autores

# Gabriel Pereira Silva

# Cassio Herbeth Rodrigues Araujo

# Funcionalidades

# Cadastro de nome, idade, peso e altura.

# Validação dos dados informados.

# Cálculo automático do IMC.

# Classificação do resultado.

# Exibição de relatório do paciente.

# Testes automatizados.

# Tecnologias

# Python 3.10 ou superior.

# Biblioteca padrão do Python (dataclasses e unittest).

# Sem dependências externas.

# Estrutura do projeto

# text

# imc-poo/

# ├── main.py

# ├── paciente.py

# ├── tests/

# │   └── test\_paciente.py

# ├── .gitignore

# └── README.md

# 

# Programação Orientada a Objetos

# 

# O projeto utiliza duas classes principais:

# 

# Paciente (paciente.py): armazena os dados do paciente e realiza o cálculo, a classificação do IMC e a geração do relatório.

# SistemaIMC (main.py): gerencia a interação com o usuário e valida as entradas.

# 

# Essa organização separa as responsabilidades e facilita a reutilização, manutenção e realização de testes.

# 

# Como executar

# 

# Na pasta principal do projeto, execute:

# 

# bash

# python main.py

# 

# 

# Caso necessário, utilize python3 main.py.

# 

# Como executar os testes

# bash

# python -m unittest discover -s tests -v

# 

# Mudanças em relação ao Trabalho 1

# 

# Em relação ao código original, foram realizadas as seguintes melhorias:

# 

# POO: funções soltas foram substituídas por classes com responsabilidades específicas.

# Tratamento de erros: a divisão por zero passou a gerar uma ArithmeticException, tratada com try/except.

# Correção de bug: corrigida a comparação entre valores inteiros e strings no menu.

# Extensibilidade: novas operações, como potência, podem ser adicionadas por meio da criação de uma nova classe e seu registro na Calculadora, sem necessidade de alterar as demais operações.



# Objetivo:

# Demonstrar a refatoração do código desenvolvido no Trabalho 1, aplicando os conceitos de Programação Orientada a Objetos para melhorar a organização, manutenção, reutilização e extensibilidade do sistema.

