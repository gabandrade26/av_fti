# Gabriel da Silva Andrade
'''
Fazer um algoritmo que exiba os números múltiplos de 6 existentes na faixa de 200 a 400. Fazer utilizando laço com while e utilizando incremento de contador de 1 em 1
'''

cont = 200
while (cont <= 400):
    if (cont % 6 == 0):
        print(f"O {cont} é múltiplo de 6.")
    cont = cont + 1