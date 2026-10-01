#armazena os dados na memória (IMPERATIVO)

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso (kg): "))
altura = float(input("digite sua altura (m): "))

#FUNCIONAL
def dados(nome, idade, peso, altura):

    # calcula o IMC
    imc = peso / (altura ** 2)

# verifica a situação do usuário(IMPERATIVO)
    if imc < 18.5:
        situacao = "Paciente está abaixo do peso"
    elif imc < 25:
        situacao = "Paciente está com o peso normal"
    elif imc < 30:
        situacao = "Paciente está acima do peso"
    else:
        situacao = "Paciente está com obesidade"

# retorna os dados
    return f"""Nome: {nome}
Idade: {idade}
Peso: {peso} kg
Altura: {altura} m
IMC: {imc:.2f}
Situação: {situacao}"""


# chama a função (IMPERATIVO)
resultado = dados(nome, idade, peso, altura)

# resultado
print("\nCadastro")
print(resultado)
