#Recebendo os dados
num1 = float(input("Digite o primeiro numero: ").replace(".",","))
num2 = float(input("Digite o valor a ser elevado: ").replace(".,",","))

#Processando os dados
resultado = num1 ** num2


#Visualização final
print("O resultado de",num1,"elevado a",num2,"é=",resultado)