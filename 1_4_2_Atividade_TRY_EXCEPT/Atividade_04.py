#Entrada de dados
try:
    nota1 = float(input("Digite a Primeira Nota: ").replace(",","."))
    nota2 = float(input("Digite a Segunda Nota: ").replace(",","."))
    nota3 = float(input("Digite a Terceira Nota: ").replace(",","."))

    #Tratamento de dados
    
    MediaFinal= float((nota1+nota2+nota3) / 3)
    
#Exibição
    print("A Média final é: ",str(MediaFinal).replace(".",","))

#Validação da nota do aluno
    if MediaFinal >= 7.0:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")

except:
 print("Valor informada inválido! Por favor digite apenas números.")


