class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
      self._titulo = titulo
      self._autor = autor
      self._ano_publicacao = ano_publicacao
      self._disponivel = True

  def __str__(self):
     return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'
  
  def emprestar(self):
      self._disponivel = False

  @staticmethod
  def verificar_disponibilidade(ano):
      livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
      return livros_disponiveis
  
livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

Livro.livros = [livro1, livro2, livro3]