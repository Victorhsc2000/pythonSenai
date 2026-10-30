try:
    idade = int(input("Digite sua idade em anos: "))

    if   idade <=0:
        print("Idade Inválida!")
    elif idade <=12:
        print("Voce é Uma Criança")
    elif idade >=13 and idade <=17:
        print("Voce é Um Adolescente")
    else:
         print("Voce é um Adulto!")
except:
    print("Idade Inválida , Por Favor Digite apenas Números!")