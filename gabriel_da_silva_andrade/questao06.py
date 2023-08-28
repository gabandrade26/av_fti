# Gabriel da Silva Andrade
'''
Fazer um algoritmo que pergunte um número positivo, e utilizando laço com while, exiba na tela a lista de números de 1 até o número informado
'''

num = float(input("Me informe um número positivo:"))
cont = 1
if (num > 0):
    print(f"Aqui a lista entre 1 e {num:.0f}:")
    while (cont <= num):
        print(cont)
        cont = cont + 1
else:
    print(f"O {num} não é positivo.")