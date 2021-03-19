class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Esta função toma o atributo idade do objeto/instância
    # para uma expressão matemática e assim poder descobrir o ano
    # de nascimento de qualquer objeto/instância Pessoa
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # @classmethod serve para criar um método que opera nas classes
    # e não nas instâncias
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

'''
p1 = Pessoa('Gabi', 22)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
p1 = Pessoa.por_ano_nascimento('Ana', 1987)
'''

p1 = Pessoa('Graze', 18)
print(f'{p1.nome} tem {p1.idade} anos de idade e nasceu em:')
p1.get_ano_nascimento()