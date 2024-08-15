from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_pizza = Restaurante('Pizza suprema', 'Comida italiana')
bebida_suco = Bebida('Suco de caju', 8.0, 'grande')
prato_paozinho = Prato('paozinho', 2.0, 'o melhor paozinho da cidade')

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()

'''usado para mostrar que é o arquivo principal e que não deve ser importado'''