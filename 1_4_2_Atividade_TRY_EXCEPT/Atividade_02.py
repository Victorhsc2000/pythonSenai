try:                
    num1 = int(input("Digite o primeiro valor: ").replace(",","."))
    num2 = int(input("Digite o segundo valor: ").replace(",","."))
    resultado = num1 + num2
    print("O resultado de",num1,"+",num2,"é de",resultado)
except:
    print("Valor informada inválido! Por favor digite apenas números.")