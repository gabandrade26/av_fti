# Gabriel da Silva Andrade
'''
Fazer um algoritmo que pergunte o valor de um produto e apresente como resposta quanto este produto vai custar numa promoção com 30% de desconto.
'''

valor = float(input("Qual o valor desse produto?"))
promo = valor - (valor * 30/100)
texto_promo = f"R$ {promo:_.2f}"
texto_promo_br = texto_promo.replace(".",",").replace("_",".")
print(f"Esse será o valor do produto com desconto de 30%: {texto_promo_br}.")