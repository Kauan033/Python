print("-----Veja o faturamento da sua empresa-----")
print("Gostaria de informar o nome da empresa? S ou N:")
opcao = str(input("Informe S ou N:\n"))
if opcao in ["S","s","sim","SIM","Sim"]:
    nome_empresa = str(input("Nome da empresa:\n"))
    faturamento = int(input("Faturamento da empresa:\n"))
    custo = int(input("Valor dos custos:\n"))
    lucro = faturamento - custo
    margem = lucro / faturamento
    print("O lucro da empresa",nome_empresa,"foi de:",lucro,"e a margem de lucro foi de:",margem*100,"%")
elif opcao in ["N","n","não","Não","NÃO","nao","Nao","NAO"]:
    faturamento = int(input("Faturamento da empresa:\n"))
    custo = int(input("Valor dos custos:\n"))
    lucro = faturamento - custo
    margem = lucro / faturamento    
    print("O lucro da empresa foi de:",lucro,"e a margem de lucro foi de:",margem*100,"%")
else:
    print("Selecão inválida!!!")
    exit()