#Recebendo os dados
num1 = float(input("Digite o primeiro número da soma: ").replace(",","."))
num2 = float(input("Digite o seundo número da soma: ").replace(",","."))


#Processando os dados
resultado = num1 + num2
resultado2 = resultado ** (1/2)


#Visualização final
print("O resultado de",str(num1).replace(".",","),"+",str(num2).replace(".",","),"elevado a Raiz Quadrada é",str(resultado2).replace(".",","))