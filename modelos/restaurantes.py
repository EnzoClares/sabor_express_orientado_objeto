class restaurante:
  def __init__(self, nome, categoria):
      self.nome = nome
      self.categoria = categoria
      self.ativo = False

restaurante_praça = restaurante('Praça', 'Comida italiana')

restaurante_pizza = restaurante('Pizza express', 'Comida italiana')

restaurantes = [restaurante_praça, restaurante_pizza]

print(vars(restaurante_praça))
print(vars(restaurante_pizza))
