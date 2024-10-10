for i in range(3):
    nome = str(input("Digite o seu nome:\n"))
    altura = float(input("Digite a sua altura:\n"))
    idade = int(input("Digite a sua idade:\n"))
    peso = float(input("Digite o seu peso:\n"))
    print("Seja bem vindo",nome,"!!!")
    print("A sua altura é de:",altura)
    print("A sua idade é de:",idade)
    print("O seu peso é de:",peso)
    print("--------------------------------------")
    
escolha = str(input("Deseja calcular o seu IMC?"))
if escolha != "sim" and escolha != "não":
    exit()



