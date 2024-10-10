salariominino = 1412
seu_salario = float(input("Informe o seu salário:\n"))
diferenca = (salariominino - seu_salario)
if seu_salario < salariominino:
    print("O salário",salariominino,"está abaixo do esperado!!!")
    print("A diferença do seu salário para o valor do piso salarial é de:",diferenca)
    print("consulte o RH com urgência!!!")
else:
    print("Você ganha um salário mínimo ou mais!!!")
    print("A diferença do seu salário para o valor do piso salarial é de:",diferenca*-1)