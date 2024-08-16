from modelos.cardapio.item import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return f'{self._nome} | {self._preco} | {self.descricao}'