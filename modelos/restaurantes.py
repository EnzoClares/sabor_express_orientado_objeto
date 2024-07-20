class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
      self.nome = nome
      self.categoria = categoria
      self._ativo = False
      Restaurante.restaurantes.append(self)
  def __str__(self):
      return f'{self.nome} | {self.categoria}'
  
  def listar_restaurantes():
      print(f'{'nome do restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'status'}')
      for restaurante in Restaurante.restaurantes:
          print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

  @property
  def ativo(self):
      return '✅' if self._ativo else '❎'

'''self é a referência da instância atual que está chamando a classe'''

restaurante_praça = Restaurante('Praça', 'Comida italiana')

restaurante_pizza = Restaurante('Pizza express', 'Comida italiana')

Restaurante.listar_restaurantes()

