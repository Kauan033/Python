print("App - Triângulo\n")
print("Primeira etapa de verificação do triângulo:")
valorum = int(input("Informe o 1° valor do triângulo: "))
valordois = int(input("Informe o 2° valor do triângulo: "))
valortres = int(input("Informe o 3° valor do triângulo: "))
equilatero = ("Todos os lados iguais")
isosceles = ("Quaisquer dois lados iguais")
escaleno = ("Três lados diferentes")

if (valorum + valordois) > valortres and (valorum + valortres) > valordois and (valordois + valortres) > valorum:
    print("Os valores informados formam um triângulo!")
    print("Segunda etapa de verificação do triângulo:")
    if valorum == valordois == valortres:
        print("A classificação do triângulo é equilátero:", equilatero)
    elif valorum == valordois or valorum == valortres or valordois == valortres:
        print("A classificação do triângulo é isósceles:", isosceles)
    else:
        print("A classificação do triângulo é escaleno:", escaleno)
else:
    print("Os valores informados não formam um triângulo!")
