from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome='', categoria=''):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao= []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
        '''serve para colocar dentro da [] restaurantes e guardar essas informações'''
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    @classmethod
    def listar_restaurantes(cls): 
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria de comida'.ljust(26)}| {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_das_avaliacoes).ljust(25)} |{restaurante.ativo}')
    '''classmethod torna o código mais legível'''
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

   
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    @property #tornar capaz de ler cada avaliação
    def media_das_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quatidade_de_notas = len(self._avaliacao)
        media_das_notas = round((soma_das_notas/quatidade_de_notas)/2, 1)
        return media_das_notas
#uso de round = arredondamento e sum = soma de valores
    def adicionar_bebida_ao_cardapio(self, bebida):
        self._cardapio.append(bebida)
    def adicionar_prato_ao_cardapio(self, prato):
        self._cardapio.append(prato)