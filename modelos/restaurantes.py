class restaurante:
  nome = ''
  categoria = ''
  ativo = True

restaurante_praça = restaurante()
restaurante_praça.nome = 'praça'
restaurante_praça.categoria = 'italiano'
restaurante_pizza = restaurante()

restaurantes = [restaurante_praça, restaurante_pizza]

print(vars(restaurante_praça))

if restaurante_praça.ativo:
  print('restaurante ativo')
else:
  print('restaurante inativo')

categoria_praça = restaurante_praça.categoria
print(categoria_praça)
restaurante_praça.nome = 'Bistrô'
print(restaurante_praça.nome)