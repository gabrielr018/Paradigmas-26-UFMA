
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
saldo = float(input("Quanto você tem de dinheiro? "))

#OPÇÕES DE BEBIDA +18
print("\n--- MENU DE BEBIDAS ---")
print("a)Cerveja Skol - R$ 10.00")
print("b)Cerveja Brahma - R$ 8.00")
print("c)Cerveja Glacial - R$ 5.00")

#QUANTIDADE
escolha = input("\nQual bebida deseja?\n")
quantidade = int(input("\nQuantas você quer?\n"))

if escolha == "a":
    preco = 10.0
elif escolha == "b":
    preco = 8.0
elif escolha == "c":
    preco = 5.0
else:
    preco = 0.0
    print("não temos essa")

#CALCULAR TOTAL DA COMPRA
total = preco * quantidade

print("\n--- RECIBO ---\n")
print(f"Cliente: {nome}")
print(f"Total a pagar: R$ {total}")

#AS 4 POSSIBILIDADES
if idade >= 18 and saldo >= total:
    print("COMPRA APROVADA! Cliente tem idade e saldo\n")

elif idade >= 18 and saldo < total:
    print("COMPRA NEGADA! Cliente tem idade, mas não tem saldo\n")

elif idade < 18 and saldo >= total:
    print("COMPRA NEGADA! Cliente tem saldo, mas não tem idade\n")

elif idade < 18 and saldo < total:
    print("COMPRA NEGADA! Cliente não tem idade e nem saldo\n")