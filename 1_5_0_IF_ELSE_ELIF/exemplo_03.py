try:
    idade = int(input("Digite sua idade em anos: "))
    if idade >65:
        print("Voce Ainda não é da terceira idade!")
    elif idade > 17:
        print("Opa Voce já é um adulto")
    else:
         print("Voce Ainda Não é um Adulto!")
except:
    print("Idade Inválida , Por Favor Digite apenas Números!")