from modelos.restaurantes import Restaurante

restaurante_pizza = Restaurante('Pizza suprema', 'Comida italiana')
restaurante_pizza.receber_avaliacao('Enzo', 7)
restaurante_pizza.receber_avaliacao('francisco', 9)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

'''usado para mostrar que é o arquivo principal e que não deve ser importado'''