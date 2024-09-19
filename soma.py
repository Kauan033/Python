print("Informe 2 números inteiros e a operação a ser feita: ")
n1 = int(input("Digite o 1° valor:" )) 
n2 = int(input("Digite o 2° valor:" ))
print("(1)-Somar","(2)-Subtrair","(3)-Multiplicar")
soma_op = "(1)-Somar"
subtrair_op = "(2)-Subtrair"
multip_op = "(3)-Multiplicar"
escolha = int(input("Informe a operação escolhida para os valores:" ))
if escolha == 1:
    print("opção",soma_op,"foi selecionada")
    print("O valor da soma dos valores é",(n1+n2))
    exit()
if escolha == 2:
    op2 = (n1-n2)
    print("O valor da subtração é",(n1-n2))
    exit()
if escolha == 3:
    op3 = (n1*n2)
    print("A multiplicação dos valores é",(n1*n2))
    exit()