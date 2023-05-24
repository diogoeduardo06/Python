Nascimento = int(input("Ano que nasceu: "))
Ano = int(input("Ano atual: "))

idade = (Ano - Nascimento)

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")