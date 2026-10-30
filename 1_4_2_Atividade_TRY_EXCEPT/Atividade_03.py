#Entrada de dados
try :
 preco_original = float(input("Digite o valor original da peça: ").replace(",","."))
 percentual_desconto = float(input("Digite o percentual de desconto ex: (20 para 20%)").replace(",","."))

#Tratamento dos dados
 valor_do_desconto = preco_original * (percentual_desconto / 100)
 preco_final = preco_original - valor_do_desconto

#Exibição Final
 print("Preço origial, R$",str(preco_original).replace(".",","))
 print("valor desconto R$", str(valor_do_desconto).replace(".",","))
 print("Preço com desconto R$", str(preco_final).replace(".",","))

except:
 print("Valor informada inválido! Por favor digite apenas números.")