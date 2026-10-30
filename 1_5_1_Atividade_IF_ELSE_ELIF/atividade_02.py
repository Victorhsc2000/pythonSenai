#Entrada de dados
try:
    nota = float(input("Digite a Nota: ").replace(",","."))
    

#Validação da nota do aluno
    
    if nota <0  or  nota >10:
        print("Nota Inválida")
    else:
        if nota >=0 and nota <4.9:
         print("Aluno Reprovado")
        elif nota >=5 and nota <=6.9:
            print("Aluno em Recuperação")
        else:
             print("Aluno Aprovado")

except:
 print("Valor informada inválido! Por favor digite apenas números.")

