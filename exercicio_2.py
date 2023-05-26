peso = float(input("Qual seu peso?: "))
altura = float(input("Qual sua altura?:"))

calculo = peso/(altura*altura)

if (calculo < 18.5):
    print("Abaixo do peso ideal")
elif (calculo >= 18.5 and calculo <= 24.9):
    print("Peso normal.")
elif (calculo >= 25 and calculo <= 29.9):
    print("Excesso de peso")
elif (calculo >= 30 and calculo <= 34.9):
    print("Obesidade nivel I")
elif (calculo >= 35 and calculo <= 39.9):
    print("Obesidade nivel II")
else:
    print("Obesidade nivel III")