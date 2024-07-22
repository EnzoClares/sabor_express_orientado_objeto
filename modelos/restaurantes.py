class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      Restaurante.restaurantes.append(self)
  def __str__(self):
      return f'{self._nome} | {self._categoria}'
  
  def listar_restaurantes():
      print(f'{'nome do restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'status'}')
      for restaurante in Restaurante.restaurantes:
          print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante._ativo}')

  @property
  def ativo(self):
      return '✅' if self._ativo else '❎'

'''self é a referência da instância atual que está chamando a classe'''

restaurante_praça = Restaurante('Praça', 'Comida italiana')

restaurante_pizza = Restaurante('pizza express', 'Comida italiana')

Restaurante.listar_restaurantes()

