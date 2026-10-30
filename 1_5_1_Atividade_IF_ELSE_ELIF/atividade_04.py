#Entrada de dados
try:
    temperatura = float(input("Digite a temperatura em °C: ").replace(",","."))
    

#Validação e exibição da temperatura
    
    if  temperatura <0 :
        print("Congelante")
    else:
        if temperatura >=0 and temperatura <=14:
         print("Frio")
        elif temperatura >=15 and temperatura <=30:
            print("Agradavel")
        else:
         temperatura >=30
         print("Muito Quente")

except:
 print("Valor informada inválido! Por favor digite apenas números.")

