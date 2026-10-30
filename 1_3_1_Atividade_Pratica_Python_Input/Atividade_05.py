#Recebendo os dados
num1 = float(input("Digite o primeiro numero: ").replace(",","."))
num2 = float(input("Digite o valor a ser elevado: ").replace(",","."))

#Processando os dados
resultado = num1 ** num2


#Visualização final
print("O resultado de",str(num1).replace(".",","),"elevado a",str(num2).replace(".",","),"é=",str(resultado).replace(".",","))