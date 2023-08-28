# Gabriel da Silva Andrade
'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 10, entre 10 e 50 ou acima de 50
'''

num = float(input("Me informe um número:"))
if (num < 10):
    print(f"O {num} está abaixo de 10.")
elif (10 <= num <= 50):
    print(f"O {num} está entre 10 e 50.")
else:
    print(f"O {num} está acima de 50.")