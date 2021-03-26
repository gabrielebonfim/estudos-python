
class A:
    vc = 123


a1 = A()
a2 = A()
a3 = A()


a1.vc = 321  # aplica a variável de classe, mas modifica o valor original apenas nesta instância

print(a1.__dict__)  # retorna {'vc': 321} - pois logo acima foi atribuído a variável de classe nesta instância
print(a2.__dict__)  # retorna {} - pois a variável de classe não foi atribuída a esta instância
print(a3.vc)  # retorna o valor original da variável de classe: 123
# pois a variável de classe está disponível a todas as instâncias


class B:
    var_class = 123

    def __init__(self):
        self.var_class = 321


b1 = B()

print(b1.var_class)  # Retorna '321', pois alterando a variável de classe no init altera para todas as instâncias
print(B.var_class)  # Retorna '123', pois a mudança de valor no init não influencia o valor original em classe
