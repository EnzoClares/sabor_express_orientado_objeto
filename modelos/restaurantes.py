class restaurante:
  nome = ''
  categoria = ''
  ativo = False

restaurante_praça = restaurante()
restaurante_praça.nome = 'praça'
restaurante_praça.categoria = 'italiano'
restaurante_pizza = restaurante()

restaurantes = [restaurante_praça, restaurante_pizza]

print(vars(restaurante_praça))