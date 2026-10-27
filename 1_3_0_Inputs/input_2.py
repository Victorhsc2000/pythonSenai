#Recebendo dados usando o input

#Receber o nome do usuário
nome = str(input("Digite seu nome completo: "))

#Receber a idade do usuario
idade = int(input("Digite sua idade em anos: "))

#Receber o peso do  usuario
#Replace adicionado para alteração de virgula para ponto caso o usuario digite virgula
peso = float(input("Digite seu peso em Kg: ").replace(",","."))

#Visualizar o nome digitado
print("O nome do usuario é: ", nome)
print("A idade do usuario é: ", idade,"anos")
print("O Peso do usuario é: ", str(peso).replace(".",","),"kg")