class restaurante:
  def __init__(self, nome, categoria):
      self.nome = nome
      self.categoria = categoria
      self.ativo = False
  def __str__(self):
      return f'{self.nome} | {self.categoria} | {self.ativo}'

'''self é a referência da instância atual que está chamando a classe'''

restaurante_praça = restaurante('Praça', 'Comida italiana')

restaurante_pizza = restaurante('Pizza express', 'Comida italiana')

restaurantes = [restaurante_praça, restaurante_pizza]

print(restaurante_praça)
print(restaurante_pizza)