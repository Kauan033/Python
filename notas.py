print("-----Calculador de médias-----")
nome = str(input("Nome do aluno: "))
idade = str(input("Idade do aluno: "))
nota1 = float(input("Informe a 1° nota do aluno: "))
nota2 = float(input("Informe a 2° nota do aluno: "))
nota3 = float(input("Informe a 3° nota do aluno: "))
media_notas = (nota1 + nota2 + nota3) / 3
maior_nota = max(nota1,nota2,nota3)
menor_nota = min(nota1,nota2,nota3)
print(maior_nota,"foi a maior nota do aluno",nome)
print(menor_nota,"foi a menor nota do aluno",nome)
print("E a sua média foi de:",round(media_notas,1))