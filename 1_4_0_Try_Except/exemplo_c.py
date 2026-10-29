try:                
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    resultado = num1 / num2
    print("O resultado de",num1,"Dividido por",num2,"é de",resultado)
except ValueError:
    print("Valor informada inválido! Por favor digite apenas números.")
except ZeroDivisionError:
    print("Erro! Não é possivel dividir por ZERO.")