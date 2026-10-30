#Entrada de dados
try:
    valor = float(input("Digite o Valor $ da Peça: ").replace(",","."))
    

#Validação do preço do produto
    
    if valor <=0 :
        print("Compra Inválida")
    else:
        if valor <=100:
         print("Sem Desconto")
        elif valor >100 and valor <=500:
            print("Desconto de 10%")
        else:
             print("Desconto de 15%")

except:
 print("Valor informada inválido! Por favor digite apenas números.")

