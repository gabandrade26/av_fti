# Gabriel da Silva Andrade
'''
Fazer um algoritmo que pergunte ao aluno 5 números e exiba como resposta a média aritmética deste 5 números e a informação se o aluno está aprovado ou reprovado. Considere média maior ou igual a 70 para aprovação.
'''

num1 = float(input("Qual foi sua nota?"))
num2 = float(input("Qual foi sua nota?"))
num3 = float(input("Qual foi sua nota?"))
num4 = float(input("Qual foi sua nota?"))
num5 = float(input("Qual foi sua nota?"))
media = (num1 + num2 + num3 + num4 + num5) / 5
if (media < 70):
    print(f"Sua média é {media} e você não foi aprovado.")
else:
    print(f"Sua média é {media}. Parabéns, você foi aprovado.")