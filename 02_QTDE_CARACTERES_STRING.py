# LEMBRANDO QUE ESSE MÉTODO SÓ FUNCIONA COM STRING
# NÃO FUNCIONA COM NUM, INT, FLOAT, OU BOOL

usuario = input('Digite seu usuário: ')
qtde_caracteres = len(usuario)
print(qtde_caracteres)

if qtde_caracteres < 6:
    print('Precisa pelo menos ter 6 caracteres')

else:
    print('Cadastro OK')


#UTILIZANDO METODO

string1 = input('Digite: ')
string2 = input('Digite: ')

print(string1.__len__())

