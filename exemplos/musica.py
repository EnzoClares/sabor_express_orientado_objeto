class Musica:
    musicas = []
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self): 
        return f'{self.nome} | {self.artista} | {self.duracao}' 

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica(nome='levanta e anda', artista='emicida', duracao=180)

