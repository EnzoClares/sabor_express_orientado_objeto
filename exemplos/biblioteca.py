from exemplos.livro import Livro
livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f'Livro antes de emprestar (biblioteca): disponivel ? {livro_biblioteca._disponivel}')
livro_biblioteca.emprestar()
print(f'Livro depois de emprestar (biblioteca): disponivel ? {livro_biblioteca._disponivel}')