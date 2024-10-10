print("Operação básica")
usersalario = float(input("Escreva o valor do seu salário:"))
if usersalario < 0   :
    exit()
else:
    aumento = float(input("Informe o percentual de aumento que recebeu:"))
    percentual = aumento / 100
    salárioaumento = (usersalario*percentual)
    print("O valor total do seu valor foi de:","$",salárioaumento)