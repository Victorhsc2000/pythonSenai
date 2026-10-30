try:
    idade = int(input("Digite sua idade em anos: "))
    if idade >65:
        print("Voce Ainda não é da terceira idade!")

    else:
         print("Voce Ainda Não Faz parte da Terceira Idade!")
except:
    print("Idade Inválida , Por Favor Digite apenas Números!")