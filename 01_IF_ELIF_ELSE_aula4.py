"""
valor = 100

if valor == 80:
    print('O número é 80')

elif valor <80:
    print('O número é menor que 80')

else:
    print('O número não é nem menor ou igual a 80')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f'Olá {nome}. Sua idade é {idade}')

if idade >= 18:
    print('Você pode consumir este conteúdo.')

else:
    print('Infelizmente você não poderá consumir este conteúdo se a presença dos pais.')

"""

valor1 = int(input('Digite um valor inteiro: '))
valor2 = int(input('Digite outro valor inteiro: '))

if valor1 and valor2 == 10:
    print('Os dois valores são iguais a 10')

elif valor1 == valor2:
    print('Os dois valores são iguais, mas não iguais a 10')

else:
    print('Os dois valores se divergem')