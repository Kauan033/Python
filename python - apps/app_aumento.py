print("App - aumento de salário\n")
seu_salario = float(input("Informe o seu salário: \n"))
if seu_salario <= 1600:
    reajuste = (seu_salario*0.20)
    novo_salario = (seu_salario + reajuste)
    print("Salário sem o reajuste é:",seu_salario)
    print("O valor do reajuste que irá receber de acordo com o valor é de:","20%")
    print("Seu novo salário com o reajuste de 20% é de:","R$",novo_salario)

elif seu_salario > 1600 and seu_salario <= 2500:
    reajuste = (seu_salario*0.15)
    novo_salario = (seu_salario + reajuste)
    print("Salário sem o reajuste é:",seu_salario)
    print("O valor do reajuste que irá receber de acordo com o valor é de:","15%")
    print("Seu novo salário com o reajuste de 15% é de:","R$",novo_salario)   

elif seu_salario > 2500 and seu_salario <= 5000:
    reajuste = (seu_salario*0.10)
    novo_salario = (seu_salario + reajuste)
    print("Salário sem o reajuste é:",seu_salario)
    print("O valor do reajuste que irá receber de acordo com o valor é de:","10%")
    print("Seu novo salário com o reajuste de 10% é de:","R$",novo_salario)

elif seu_salario > 5000:
    reajuste = (seu_salario*0.5)
    novo_salario = (seu_salario + reajuste)
    print("Salário sem o reajuste é:",seu_salario)
    print("O valor do reajuste que irá receber de acordo com o valor é de:","5%")
    print("Seu novo salário com o reajuste de 5% é de:","R$",novo_salario)
    
else:
    print("valor informado inválido!")
    exit()