# PROGRAMAÇÃO ORIENTADA A OBJETOS

class OperacaoAritmetica:
  
  def __init__(self, valor_a, valor_b):
    self.valor_a = valor_a
    self.valor_b = valor_b

  def soma(self):
    return self.valor_a + self.valor_b

  def subtracao(self):
    return self.valor_a - self.valor_b

  def multiplicacao(self):
    return self.valor_a * self.valor_b

  def divisao(self):
    return self.valor_a / self.valor_b

  def resto(self):
    return self.valor_a % self.valor_b

  def exponenciacao(self):
    return self.valor_a ** self.valor_b

  def divisao_inteira(self):
    return self.valor_a // self.valor_b


a = OperacaoAritmetica(10, 3)

print("soma:", a.soma())
print("subtracao:", a.subtracao())
print("multiplicacao:", a.multiplicacao())
print("divisao:", a.divisao())
print("resto:", a.resto())
print("exponenciacao:", a.exponenciacao())
print("divisao_inteira:", a.divisao_inteira())