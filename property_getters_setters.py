
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter - Usado para pegar o valor, que no caso é uma string
    @property
    def preco(self): # O método leva o mesmo nome da variável
         return self._preco # essa variável leva o mesmo, mas acompanhado de _ para não dar bugs

    # Setter - Usado para configurar o valor pego pelo getter
    @preco.setter
    def preco(self, valor):  # Valor é o resultado já formatado que será enviado para 'self.preco' lá em cima
        if isinstance(valor, str):  #Checa se o 'valor' é uma instância do tipo 'string'
            valor = float(valor.replace('R$', ''))  # Elimina o 'R$' do valor e transforma a numeração em 'float'
                                                     # O replace também serve para substituir caracteres de alguma string
        self._preco = valor


p1 = Produto('Blazer', 'R$40')
p1.desconto(50)
print(p1.preco)

'''
Nessa situação, o replace só é útil neste caso específico. Em outros casos
é necessário a utilização de expressões regulares. 
Mas basicamente, o que aprendemos aqui é que @property é utilizado 
para realizar getters - ou seja, coletar valores - e @variavel.setter
serve para realizar a configuração desta variável antes mesmo dela
ser operalizada no método __init__

'''