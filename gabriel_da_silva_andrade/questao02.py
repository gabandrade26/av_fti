# Gabriel da Silva Andrade
'''
Fazer um algoritmo que pergunte um número. Se o usuário inserir 1 deverá aparecer a mensagem "Bom dia!". Se for 2 "Boa Tarde!". Se for 3 "Boa Noite!". Para qualquer outro número deve aparecer a mensagem "Tchau!".
'''

num = int(input("Insira um número para saber sua mensagem pedida:"))
if (num == 1):
    print("Bom dia!")
elif (num == 2):
    print("Boa Tarde!")
elif (num == 3):
    print("Boa Noite!")
else:
    print("Tchau!")