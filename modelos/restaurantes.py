class Restaurante:
    restaurantes = []
    def __init__(self, nome='', categoria=''):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
        '''serve para colocar dentro da [] restaurantes e guardar essas informações'''
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria de comida'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    '''classmethod torna o código mais legível'''
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'


restaurante_pizza = Restaurante('Pizza suprema', 'comida italiana')
restaurante_japones = Restaurante('sushi loko', 'comida japonesa')

Restaurante.listar_restaurantes()