print("Desenvolva um programa que recebe um número do teclado e mostre se o número é positivo ou negativo")
n1 = int(input("\nInforme o número a ser verificado: "))
if n1 > 0:
    print("Número positivo")
elif n1 == 0:
    print("Número nulo")
else:
    print("Número negativo")