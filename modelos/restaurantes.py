class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
      self.nome = nome
      self.categoria = categoria
      self.ativo = False
      Restaurante.restaurantes.append(self)
  def __str__(self):
      return f'{self.nome} | {self.categoria} | {self.ativo}'
  
  def listar_restaurantes():
      for restaurante in Restaurante.restaurantes:
          print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

'''self é a referência da instância atual que está chamando a classe'''

restaurante_praça = Restaurante('Praça', 'Comida italiana')

restaurante_pizza = Restaurante('Pizza express', 'Comida italiana')

Restaurante.listar_restaurantes()