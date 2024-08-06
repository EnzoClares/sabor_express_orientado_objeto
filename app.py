from modelos.restaurantes import Restaurante

restaurante_pizza = Restaurante('Pizza suprema', 'Comida italiana')
restaurante_japones = Restaurante('japa', 'Comida japonesa')
restaurante_mexicano = Restaurante('Mexirico', 'Comida mexicana')
restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()