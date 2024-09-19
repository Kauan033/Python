print("-----Seja bem vindo ao calculador de IMC-----")
for i in range(5):
    nome = str(input("Digite o seu nome:" ))
    idade = int(input("Digite a sua idade:" ))
    altura = float(input("Digite a sua altura:" ))
    peso = float(input("Digite o seu peso:" ))
    calculoimc = peso / (altura*altura)
    print(nome,"com",idade,"anos","possui o imc de:",round(calculoimc,2)) 